from book_api.books.models import Category
from book_api.repository.CategoryRepository import CategoryRepository


class CategoryRepositoryImpl(CategoryRepository):
    def get_or_create(self, name: str):
        return Category.objects.get_or_create(name=name)[0]