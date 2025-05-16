from extract.extract import CsvExtractor
from load.load import JsonLoader
from transform.transform import Deduplicator

class Job:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        self.CsvExtractor = CsvExtractor()
        self.Deduplicator = Deduplicator()
        self.JsonLoader = JsonLoader()
        
    def run(self):
        source_data = self.CsvExtractor.extract(self.input_path)
        transformed_data = self.Deduplicator.transform(source_data)
        self.JsonLoader.load(transformed_data, self.output_path)