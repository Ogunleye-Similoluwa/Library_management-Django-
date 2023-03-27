from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum
from django_enumfield import enum


# Create your models here.
class LibraryUser(AbstractUser):
    app = models.IntegerField
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=400, null=False, blank=False)
    last_name = models.CharField(max_length=400, null=False, blank=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(null=False, blank=False)
    date_of_death = models.DateField(null=True, blank=True, default='0000-00-0')

    def __str__(self):
        return f"{self.first_name}---{self.last_name}"


# class Genre(models.Model):
#     STATUS_CHOICES = [
#         ('FICTION', 'fic'),
#         ('COMEDY', 'com'),
#         ('ROMANCE', 'rom')
#     ]
#     # name = models.CharField(max_length=10, choices=STATUS_CHOICES, default='com')
#     name = models.enums.Choices(STATUS_CHOICES)
#
#     def __str__(self):
#         return self.name


# class Language(models.Model):
#     STATUS_CHOICES = [
#         ('ENGLISH', 'ENG'),
#         ('FRENCH', 'FRE')
#     ]
#
#     name = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ENG')
#
#     def __str__(self):
#         return self.name
#
#
# class Genre(models.Model):
#     STATUS_CHOICES = [
#         ('FICTION', 'FIC'),
#         ('DRAMA', 'DRA'),
#         ('ROMANCE', 'rom')
#     ]
#     name = models.CharField(max_length=10, choices=STATUS_CHOICES, default='FIC')
#
#     def __str__(self):
#         return self.name
#

class Book(models.Model):
    GENRE_CHOICES = [
        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('POWER', 'POW'),
        ('COMEDY', 'COM'),
    ]
    LANGUAGE_CHOICES = [
        ('YORUBA', 'YOR'),
        ('IGBO', 'IGB'),
        ('HAUSA', 'HAU'),
        ('ENGLISH', 'ENG')
    ]
    title = models.CharField(max_length=400, null=False, blank=False)
    isbn = models.CharField(max_length=13, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='FIC')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='ENG')
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title}---{self.date_added}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    uniqueId = models.UUIDField(primary_key=True, default=uuid4)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=400, null=False, blank=False)

    # borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE, name='borrower')

    def __str__(self):
        return self.imprint
