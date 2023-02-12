class Link:
    __slots__ = ('url', 'title')

    def __init__(
            self,
            *,
            url: str,
            title: str
    ):
        self.url = url
        self.title = title
