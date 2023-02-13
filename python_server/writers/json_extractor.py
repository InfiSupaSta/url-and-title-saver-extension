import json
from typing import Union, Tuple


class JSONExtractor:
    @staticmethod
    def extract(data: bytes) -> Tuple[Union[str, None], Union[str, None]]:
        json_to_dict = json.loads(data)
        title = json_to_dict.get('title')
        url = json_to_dict.get('url')
        return title, url
