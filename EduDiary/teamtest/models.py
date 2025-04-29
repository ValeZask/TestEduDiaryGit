from django.db import models

# Create your models here.
# Hello World
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    