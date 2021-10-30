from typing import Iterable

import pytest as pytest

from ebook_clippings.clippings import BookClippings, Clipping


@pytest.fixture
def expected_clippings_iterable() -> Iterable[BookClippings]:
    return [
        BookClippings(
            book_name="An Astronaut's Guide to Life on Earth",
            book_author="Chris Hadfield",
            clippings=[
                Clipping(
                    clipping_location="137-138",
                    clipping_content="It's probably not going to happen, but I should do things that keep me moving in the right direction, just in case—and I should be sure those things interest me, so that whatever happens, I'm happy.",
                    datetime="Thursday, 31 January 2019 00:11:39",
                ),
                Clipping(
                    clipping_location="545-548",
                    clipping_content="Taking the attitude that I might never get to space—and then, after I did get there, that I might never go back—helped me hold onto that feeling for more than two decades. Because I didn't hang everything—my sense of self-worth, my happiness, my professional identity—on space flight, I was excited to go to work every single day, even during the 11 years after my second mission when I didn't fly and was, at one point, told definitively that I never would again (more on that later).",
                    datetime="Thursday, 31 January 2019 19:14:20",
                ),
                Clipping(
                    clipping_location="552-556",
                    clipping_content="Success is feeling good about the work you do throughout the long, unheralded journey that may or may not wind up at the launch pad. You can't view training solely as a stepping stone to something loftier. It's got to be an end in itself. The secret is to try to enjoy it. I never viewed training as some onerous duty I had to carry out while praying fervently for another space mission. For me, the appeal was similar to that of a New York Times crossword puzzle: training is hard and fun and stretches my mind, so I feel good when I persevere and finish—and I also feel ready to do it all over again.",
                    datetime="Thursday, 31 January 2019 19:15:46",
                ),
                Clipping(
                    clipping_location="562-564",
                    clipping_content="There's really just one thing I can control: my attitude during the journey, which is what keeps me feeling steady and stable, and what keeps me headed in the right direction. So I consciously monitor and correct, if necessary, because losing attitude would be far worse than not achieving my goal.",
                    datetime="Thursday, 31 January 2019 21:54:42",
                ),
                Clipping(
                    clipping_location="574-576",
                    clipping_content="To me, it's simple: if you've got the time, use it to get ready. What else could you possibly have to do that's more important? Yes, maybe you'll learn how to do a few things you'll never wind up actually needing to do, but that's a much better problem to have than needing to do something and having no clue where to start.",
                    datetime="Thursday, 31 January 2019 21:56:12",
                ),
            ],
        ),
        BookClippings(
            book_name="Homo Deus: A Brief History of Tomorrow",
            book_author="Yuval Noah Harari",
            clippings=[
                Clipping(
                    clipping_location="3025-3028",
                    clipping_content="On the practical level, modern life consists of a constant pursuit of power within a universe devoid of meaning. Modern culture is the most powerful in history, and it is ceaselessly researching, inventing, discovering and growing. At the same time, it is plagued by more existential angst than any previous culture.",
                    datetime="Wednesday, 16 January 2019 00:24:32",
                ),
                Clipping(
                    clipping_location="3056-3058",
                    clipping_content="In the Middle Ages, the outbreak of a plague caused people to raise their eyes towards heaven, and pray to God to forgive them for their sins. Today, when people hear of some new deadly epidemic, they pick up the phone and call their broker. For the stock exchange, even an epidemic is a business opportunity.",
                    datetime="Wednesday, 16 January 2019 00:29:52",
                ),
                Clipping(
                    clipping_location="3124-3125",
                    clipping_content="Since economic growth is allegedly the source of all good things, it encourages people to bury their ethical disagreements and adopt whichever course of action maximises long-term growth.",
                    datetime="Wednesday, 16 January 2019 00:40:20",
                ),
                Clipping(
                    clipping_location="3195-3197",
                    clipping_content="The greatest scientific discovery was the discovery of ignorance. Once humans realised how little they knew about the world, they suddenly had a very good reason to seek new knowledge, which opened up the scientific road to progress.",
                    datetime="Thursday, 17 January 2019 00:02:01",
                ),
                Clipping(
                    clipping_location="3298-3301",
                    clipping_content="Although we experience occasional economic crises and international wars, in the long run capitalism has not only managed to prevail, but also to overcome famine, plague and war. For thousands of years priests, rabbis and muftis explained that humans cannot overcome famine, plague and war by their own efforts. Then along came the bankers, investors and industrialists,",
                    datetime="Thursday, 17 January 2019 00:18:37",
                ),
            ],
        ),
    ]
