from dataclasses import dataclass


@dataclass
class BookDto:
    title: str
    authors: list
    published_date: str
    categories: list
    average_rating: float
    ratings_count: int
    thumbnail: str