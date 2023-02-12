from writers.base_writer import BaseWriter
from writers.json_extractor import JSONExtractor
from db import Link, InsertRow


class SQLiteWriter(BaseWriter, JSONExtractor):

    def write(
            self,
            data: bytes,
    ):
        title, url = self.extract(data)
        while '"' in title:
            title.replace('"', "'")
        if all(
                [title is not None, url is not None]
        ):
            with InsertRow() as sql:
                link = Link(
                    url=url,
                    title=title
                )
                sql.insert_row(link)
