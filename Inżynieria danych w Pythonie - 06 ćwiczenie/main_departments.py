from extract.extract import CsvExtractor
from department_count.counting import Counting
from ParquetLoader.loader import ParquetLoader
from job_etapIII import Job
import sys

if __name__ == '__main__':

    job = Job( 
        sys.argv[1],
        sys.argv[2],
        extractor=CsvExtractor(),
        counter = Counting(),
        loader= ParquetLoader()
    )
    job.run()
