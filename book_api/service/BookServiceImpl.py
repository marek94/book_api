from book_api.api.BookApi import BookApi
from book_api.books.models import Book
from book_api.dto.BookDto import BookDto
from book_api.repository.AuthorRepository import AuthorRepository
from book_api.repository.BookRepository import BookRepository
from book_api.repository.CategoryRepository import CategoryRepository
from book_api.service.BookService import BookService
from book_api.utils.book_utils import get_book_authors_by_name, get_book_categories_by_name


class BookServiceImpl(BookService):

    def __init__(self, book_repository: BookRepository, author_repository: AuthorRepository,
                 category_repository: CategoryRepository, book_api: BookApi):
        self.book_repository = book_repository
        self.author_repository = author_repository
        self.category_repository = category_repository
        self.book_api = book_api

    def get_book_by_id(self, id: int):
        try:
            book = self.book_repository.get_book_by_id(id)
            return BookDto(title=book.title, authors=get_book_authors_by_name(book),
                           categories=get_book_categories_by_name(book), published_date=str(book.published_date),
                           average_rating=book.average_rating, ratings_count=book.ratings_count,
                           thumbnail=book.thumbnail).__dict__
        except Book.DoesNotExist:
            return {}

    def get_books(self, **kwargs):
        response = []

        books = self.book_repository.get_books(**kwargs)
        for book in books:
            response.append(
                BookDto(title=book.title, authors=get_book_authors_by_name(book),
                        categories=get_book_categories_by_name(book), published_date=str(book.published_date),
                        average_rating=book.average_rating, ratings_count=book.ratings_count,
                        thumbnail=book.thumbnail).__dict__)
        return response

    def get_book_by_year(self, year: int):
        return self.book_repository.get_books_by_year(year)

    def update_db(self, query):
        data = self.book_api.fetch_books_with_query(query)
        books = data['items']
        for book_dto in books:
            book_info = book_dto['volumeInfo']
            authors = [] if not book_info.get('authors') else [self.author_repository.get_or_create(author) for author
                                                               in book_info['authors']]
            categories = [] if not book_info.get('categories') else [
                self.category_repository.get_or_create(category.strip())
                for
                category in
                book_info['categories'][0].split(',')]
            title = book_info['title']
            published_date = book_info['publishedDate']
            average_rating = book_info.get('averageRating')
            ratings_count = book_info.get('ratingsCount', 0)
            if book_info.get('imageLinks'):
                thumbnail = book_info['imageLinks'].get('thumbnail')
            else:
                thumbnail = ''
            self.book_repository.create_or_update(title=title, authors=authors, published_date=published_date,
                                                  categories=categories, average_rating=average_rating,
                                                  thumbnail=thumbnail, ratings_count=ratings_count)
