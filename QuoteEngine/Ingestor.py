# encapsulating the sub-classes for the purpose of ingesting these file
# formats.
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """
    Convert the file formats in ingestors[] to a list of QuoteModel objects.
    """
    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
