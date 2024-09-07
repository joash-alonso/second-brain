from abc import ABC, abstractmethod
from llama_index.core import Document, SimpleDirectoryReader
from typing import List


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, reader: SimpleDirectoryReader):
        pass

    @abstractmethod
    def post_process(self):
        pass


class PDFExtractor(BaseExtractor):
    def __init__(self, num_workers: int | None = None) -> None:
        self.num_workers = num_workers

    def extract(self, reader: SimpleDirectoryReader, **kwargs) -> List[Document]:
        if not isinstance(reader, SimpleDirectoryReader):
            raise NotImplementedError(
                "Only accepting SimpleDirectoryReader from llama-index"
            )

        if not hasattr(reader, "load_data"):
            raise AttributeError("Llama-index API has changed")

        return reader.load_data(num_workers=self.num_workers or 4)

    def post_process(self):
        return None


if __name__ == "__main__":
    directory_reader = SimpleDirectoryReader(
        input_files=["sample.pdf"], required_exts=[".pdf"]
    )
    extractor = PDFExtractor()
    print(extractor.extract(reader=directory_reader))
