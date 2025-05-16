from extract.extract import CsvExtractor
from ParquetLoader.loader import ParquetLoader
from transform.transform import Deduplicator

class Job:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.CsvExtractor = CsvExtractor()
        self.Deduplicator = Deduplicator()
        self.ParquetLoader = ParquetLoader()
        
    def run(self):
        source_data = self.CsvExtractor.extract(self.input_path)
        transformed_data = self.Deduplicator.transform(source_data)
        self.ParquetLoader.load(transformed_data, self.output_path)