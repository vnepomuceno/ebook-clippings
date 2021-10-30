from ebook_clippings.clippings import ClippingsService


class TestImport:
    @staticmethod
    def test_get_clippings(expected_clippings_iterable):
        clippings_service = ClippingsService(
            clippings_filepath="tests/resources/MyClippings.txt",
            json_filepath="tests/resources/clippings.json",
        )
        clippings = clippings_service.get_clippings()
        assert clippings == expected_clippings_iterable
