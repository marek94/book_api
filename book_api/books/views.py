from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book_api.books.models import Book

from book_api.di.providers import provide_book_service
from book_api.dto.BookDto import BookDto
from book_api.service.BookService import BookService


@api_view()
def get_books(request, book_service: BookService = provide_book_service()):
    params = request.query_params
    authors = params.getlist('author')
    published_date = params.getlist('published_date')
    sort = params.get('sort', '')
    return Response(book_service.get_books(authors=authors, published_date=published_date, sort=sort))



@api_view()
def get_book(request, book_id, book_service: BookService = provide_book_service()):
    return Response(book_service.get_book_by_id(book_id))


@api_view(['POST'])
def set_books(request, book_service: BookService = provide_book_service()):
    data = request.data
    query = data.get('q')
    if not query:
        return Response(status=400)
    book_service.update_db(query)
    return Response()