from django.urls import path

from book_api.book_api.books import views

urlpatterns = [
    path('', views.index, name='index'),
]