from abc import ABC, abstractmethod


class BookService(ABC):
    @abstractmethod
    def get_books(self, **kwargs): pass

    @abstractmethod
    def get_book_by_id(self, id: int): pass

    @abstractmethod
    def get_book_by_year(self, year: int): pass

    @abstractmethod
    def update_db(self, query): pass
