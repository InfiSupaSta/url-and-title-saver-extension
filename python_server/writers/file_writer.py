import pathlib

from writers.base_writer import BaseWriter
from writers.json_extractor import JSONExtractor

BASE_DIR = pathlib.Path(__file__).parent.parent.parent

DEFAULT_TEXT_FILENAME = BASE_DIR.joinpath('READ_ME_ASAP.txt')
DEFAULT_SEPARATOR = '|||'


class FileWriter(BaseWriter, JSONExtractor):
    def __init__(self, filename: str = DEFAULT_TEXT_FILENAME):
        self.filename = filename

    def write(self, data: bytes):
        title, url = self.extract(data)
        with open(self.filename, 'a+') as output_file:
            output_file.write(f'{title} {DEFAULT_SEPARATOR} {url}\n')
