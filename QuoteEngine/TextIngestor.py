from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

# ingest txt file format. Create list of QuoteModel objects.


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, "r") as i:
            lines = i.readlines()

        for row in lines:
            quote, author = row.split('-')
            quotes.append(QuoteModel(quote.strip(), author.strip()))

        return quotes
