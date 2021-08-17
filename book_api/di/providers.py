from book_api.api.BookApi import BookApi
from book_api.api.BookApiImpl import BookApiImpl
from book_api.repository.AuthorRepository import AuthorRepository
from book_api.repository.AuthorRepositoryImpl import AuthorRepositoryImpl
from book_api.repository.BookRepository import BookRepository
from book_api.repository.BookRepositoryImpl import BookRepositoryImpl
from book_api.repository.CategoryRepository import CategoryRepository
from book_api.repository.CategoryRepositoryImpl import CategoryRepositoryImpl
from book_api.service.BookService import BookService
from book_api.service.BookServiceImpl import BookServiceImpl
from book_api.settings import BOOK_API_URL


def provide_book_api() -> BookApi:
    return BookApiImpl(BOOK_API_URL)


def provide_book_repository() -> BookRepository:
    return BookRepositoryImpl()


def provide_author_repository() -> AuthorRepository:
    return AuthorRepositoryImpl()


def provide_category_repository() -> CategoryRepository:
    return CategoryRepositoryImpl()


def provide_book_service() -> BookService:
    return BookServiceImpl(provide_book_repository(), provide_author_repository(), provide_category_repository(), provide_book_api())