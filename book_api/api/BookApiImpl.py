import requests

from book_api.api.BookApi import BookApi


class BookApiImpl(BookApi):

    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_books_with_query(self, query: str):
        return requests.get(f'{self.api_url}?q={query}').json()
