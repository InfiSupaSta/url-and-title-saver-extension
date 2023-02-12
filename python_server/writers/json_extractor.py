import json


class JSONExtractor:
    @staticmethod
    def extract(data: bytes) -> tuple[str | None, str | None]:
        json_to_dict = json.loads(data)
        title = json_to_dict.get('title')
        url = json_to_dict.get('url')
        return title, url
