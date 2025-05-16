from typing import Protocol
import pandas as pd

class ExtractorProtocol(Protocol):

    def extract(self, path: str) -> pd.DataFrame:
        ...

class CsvExtractor(ExtractorProtocol):
    def extract(self,path: str) -> pd.DataFrame:
        return pd.read_csv(path)