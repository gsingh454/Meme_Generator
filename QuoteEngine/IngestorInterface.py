from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel

# abstract base class for the ingestors parsing the files.


class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        # checking if the file format matches
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        # method implemented in the sub-classes
        pass
