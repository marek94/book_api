from django.db.models import Q

from book_api.books.models import Book
from book_api.repository.BookRepository import BookRepository


class BookRepositoryImpl(BookRepository):
    def get_books(self, **kwargs):
        filters = None
        if kwargs.get('authors'):
            for author in kwargs['authors']:
                author = author.replace('"', '')
                filter = Q(authors__name=author)
                if not filters:
                    filters = filter
                else:
                    filters = filters & filter
        if kwargs.get('published_date'):
            for pd in kwargs['published_date']:
                filter = Q(published_date__contains=pd)
                if not filters:
                    filters = filter
                else:
                    filters = filters & filter
        result = Book.objects.filter(filters) if filters else Book.objects.all()
        if kwargs.get('sort'):
            result = result.order_by(kwargs['sort'])
        return result

    def get_books_by_year(self, year: int):
        return Book.objects.filter(published_date=year)

    def get_book_by_id(self, id: int):
        return Book.objects.get(pk=id)

    def create_or_update(self, title: str, authors, categories, **fields):
        book, created = Book.objects.update_or_create(title=title, defaults=fields)
        book.authors.set(authors)
        book.categories.set(categories)
        return book


