from abc import abstractmethod, ABC


class CategoryRepository(ABC):
    @abstractmethod
    def get_or_create(self, name: str): pass
