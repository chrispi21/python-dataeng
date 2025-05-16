from typing import Protocol
import pandas as pd

class CountingProtocol(Protocol):

    def count(self, data: pd.DataFrame) -> pd.DataFrame:
        ...

class Counting():

    def count(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.groupby('Departament')[['Imię']].count()