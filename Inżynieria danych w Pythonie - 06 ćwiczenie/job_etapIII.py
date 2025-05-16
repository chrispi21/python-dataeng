from extract.extract import CsvExtractor
from ParquetLoader.loader import ParquetLoader
from department_count.counting import Counting
class Job:
    def __init__(self, input_path: str, output_path: str, extractor: CsvExtractor, loader: ParquetLoader, counter: Counting):
        self.input_path = input_path
        self.output_path = output_path
        self.CsvExtractor = extractor
        self.Counting = counter
        self.ParquetLoader = loader
        
    def run(self):
        source_data = self.CsvExtractor.extract(self.input_path)
        transformed_data = self.Counting.count(source_data)
        self.ParquetLoader.load(transformed_data, self.output_path)