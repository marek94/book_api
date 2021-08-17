from abc import ABC, abstractmethod


class BookRepository(ABC):
    @abstractmethod
    def get_books(self, sort: str): pass

    @abstractmethod
    def get_book_by_id(self, id: int): pass

    @abstractmethod
    def get_books_by_year(self, year: int): pass

    @abstractmethod
    def create_or_update(self, title: str, authors, categories, **fields): pass
