from typing import Protocol
import pandas as pd

class ParquetLoaderProtocol(Protocol):
    def load(self, df: pd.DataFrame, path: str) -> None:
        ...

class ParquetLoader(ParquetLoaderProtocol):

    def load(self, df: pd.DataFrame, path: str) -> None:
        return df.to_parquet(path)