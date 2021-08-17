from book_api.books.models import Author
from book_api.repository.AuthorRepository import AuthorRepository


class AuthorRepositoryImpl(AuthorRepository):

    def get_or_create(self, name: str) -> Author:
        return Author.objects.get_or_create(name=name)[0]
