from abc import ABC, abstractmethod


class AuthorRepository(ABC):
    @abstractmethod
    def get_or_create(self, name: str): pass
