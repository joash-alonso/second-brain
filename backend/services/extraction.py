from abc import ABC, abstractmethod
from pathlib import Path
from llama_index.core import Document, SimpleDirectoryReader
from typing import List


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass


class SimplePDFExtractor(BaseExtractor):
    def __init__(
        self, file_paths: List[Path | str], num_workers: int | None = None
    ) -> None:
        self.file_paths = file_paths
        self.num_workers = num_workers
        self.__required_exts = ["pdf"]

    @property
    def pdf_loader(self):
        if not isinstance(self.file_paths, list):
            raise TypeError("File paths should be a list")

        return SimpleDirectoryReader(
            input_files=self.file_paths, required_exts=self.__required_exts
        )

    def extract(self) -> List[Document]:
        return self.pdf_loader.load_data(
            self.file_paths, num_workers=self.num_workers or 4
        )


if __name__ == "__main__":
    extractor = SimplePDFExtractor("sample.pdf")
    print(extractor.extract())
