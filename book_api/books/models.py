from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    published_date = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    average_rating = models.FloatField(null=True)
    ratings_count = models.IntegerField(default=0)
    thumbnail = models.URLField()
