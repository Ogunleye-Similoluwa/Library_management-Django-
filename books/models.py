from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    description = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

