from abc import ABC, abstractmethod
from pathlib import Path
from llama_index.core import Document, SimpleDirectoryReader
from typing import List


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class SimplePDFExtractor(BaseExtractor):
    def __init__(self, path: Path | str, num_workers: int | None = None) -> None:
        self.path = path
        self.num_workers = num_workers

    @property
    def pdf_loader(self):
        return SimpleDirectoryReader(input_dir=self.path)

    def extract(self) -> List[Document]:
        return self.pdf_loader.load_data(self.path, num_workers=self.num_workers or 4)
