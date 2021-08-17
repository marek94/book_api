from book_api.books.models import Book


def get_book_authors_by_name(book: Book):
    return [author.name for author in book.authors.all()]


def get_book_categories_by_name(book: Book):
    return [category.name for category in book.categories.all()]