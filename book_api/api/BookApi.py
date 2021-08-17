from abc import abstractmethod, ABC


class BookApi(ABC):
    @abstractmethod
    def fetch_books_with_query(self, query: str): pass
