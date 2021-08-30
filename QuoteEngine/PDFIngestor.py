from typing import List
from time import time
import os
import subprocess

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

# ingest PDF file format. Create list of QuoteModel objects.


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        # CLI tool - pdftotext used to convert pdf format to txt format.
        tmp = f'./tmp/{int(time())}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        with open(tmp, 'r') as f:
            quotes = []

            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) == 0:
                    continue
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        os.remove(tmp)
        return quotes
