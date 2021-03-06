import json
import logging
from dataclasses import dataclass
from typing import Iterable, Tuple, Dict, List, Callable, Optional, Union

import click as click
import coloredlogs as coloredlogs
import ftfy as ftfy

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)
logging.getLogger().setLevel(logging.DEBUG)


@dataclass
class Clipping:
    clipping_location: str
    clipping_content: str
    datetime: str


@dataclass
class BookClippings:
    book_name: str
    book_author: str
    clippings: List[Clipping]


class ClippingsService:
    def __init__(self, clippings_filepath: str, json_filepath: str):
        self.clippings_filepath = clippings_filepath
        self.separator = "=========="
        self.json_filepath = json_filepath

    @staticmethod
    def _extract_attributes(entry: str) -> Tuple[str, ...]:
        try:
            # Attribute extraction
            metadata, content = entry.split("\n\n")
            book_metadata = metadata.split("\n")[0]
            clipping_metadata = metadata.split("\n")[1]
            book_name = book_metadata.split(" (")[0].replace('"', "")
            book_author = book_metadata.split(" (")[1].replace(")", "")
            clipping_location = clipping_metadata.split(" | ")[0].split("on ")[1]
            clipping_datetime = clipping_metadata.split(" | ")[1].split("on ")[1]

            # Post-processing
            content = content.replace("\n", "")
        except Exception as exception:
            logger.error(f"Cannot extract attributes of {entry=}, raised {exception=}")

        return book_name, book_author, clipping_location, content, clipping_datetime

    def export_clippings_to_json(
        self,
        clippings: Iterable[BookClippings],
        sort_rule: Optional[Callable[[BookClippings], str]] = None,
        indent: Optional[int] = 2,
    ):
        clippings_set = {clip.book_name: clip.book_author for clip in clippings}
        logger.debug(
            f"Exporting clippings from books {json.dumps(clippings_set, indent=indent)}"
        )

        """Dump clippings to JSON"""
        if sort_rule is not None:
            clippings = sorted(clippings, key=sort_rule)
        sorted_dict_clippings = self._get_clippings_dictionary(clippings)
        json_clippings = json.dumps(sorted_dict_clippings, ensure_ascii=False, indent=2)

        """ Write JSON to output file"""
        with open(self.json_filepath, "w") as output_file:
            output_file.write(json_clippings)

        logger.info(f"Clippings successfully converted to JSON in {self.json_filepath}")

    @staticmethod
    def _get_clippings_dictionary(
        clippings: Iterable[BookClippings],
    ) -> Dict[str, Union[str, Dict[str, str]]]:
        """
        Converts an iterable of `BookClippings` into a JSON serializable dictionary.
        :param clippings: Iterable of `BookClippings` objects to be serialized.
        :return: Serializable dictionary of clippings.
        """
        clippings_dict = {}
        for item in clippings:
            clippings = [c.__dict__ for c in item.clippings]
            item.clippings = clippings
            clippings_dict[item.book_name] = item.__dict__

        return clippings_dict

    def _load_raw_clippings(self) -> Iterable[str]:
        """
        Loads raw clippings from file, processes its contents and returns an
        iterable of strings, each containing a raw clipping.
        :return: Iterable of raw clippings.
        """
        logger.info(f"Reading Kindle clippings from file {self.clippings_filepath}")

        """ Read content from file """
        with open(self.clippings_filepath) as file:
            content = file.read()

        """ Text processing and filtering """
        content = ftfy.fix_text(content)
        raw_clippings: Iterable[str] = [
            entry[1:] if entry.startswith("\n") else entry
            for entry in content.split(self.separator)
        ]
        raw_clippings = list(filter(lambda c: c != "", raw_clippings))

        return raw_clippings

    def _convert_to_dataclass_list(
        self, raw_clippings: Iterable[str]
    ) -> Iterable[BookClippings]:
        """
        Converts a list of iterable raw clippings into an iterable of objects
        of type `BookClippings`.
        :param raw_clippings: Iterable of raw clippings.
        :return: Iterable of objects of type `BookClippings`.
        """
        clippings_list: List[BookClippings] = []
        for book_name, author, location, content, date in [
            self._extract_attributes(entry) for entry in raw_clippings
        ]:
            logger.debug(
                f"Processing {book_name=}, {author=}, content='{content[:100] + '...'}'"
            )
            new_clipping = Clipping(
                clipping_location=location, clipping_content=content, datetime=date
            )
            clipping_result = [
                item for item in clippings_list if item.book_name == book_name
            ]
            if len(clipping_result) == 0:
                clippings_list.append(
                    BookClippings(
                        book_name=book_name,
                        book_author=author,
                        clippings=[new_clipping],
                    )
                )
            else:
                if len(clipping_result[0].clippings) == 0:
                    clipping_result[0].clippings = [new_clipping]
                else:
                    clipping_result[0].clippings.append(new_clipping)

        return clippings_list

    def get_clippings(self) -> Iterable[BookClippings]:
        """
        Loads raw clippings from file and returns an iterable of objects
        of type `BookClippings`.
        :return: Iterable of objects of type `BookClippings`.
        """
        raw_clippings = self._load_raw_clippings()
        clippings_list = self._convert_to_dataclass_list(raw_clippings)

        return clippings_list


@click.command()
@click.option("--input-filepath", type=str, help="File path of the raw clippings")
@click.option("--output-filepath", type=str, help="File path of the json output")
def import_clippings_command(input_filepath: str, output_filepath: str):
    clipping_service = ClippingsService(
        clippings_filepath=input_filepath,
        json_filepath=output_filepath,
    )
    clipping_list: Iterable[BookClippings] = clipping_service.get_clippings()
    clipping_service.export_clippings_to_json(
        clippings=clipping_list, sort_rule=lambda clipping: clipping.book_name
    )


if __name__ == "__main__":
    import_clippings_command()
