from abc import ABC

from rest_framework import serializers
from books.models import Book, Author


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description']


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description']


# todo when you wan  to add something that are not inside your model
# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=400)
#     last_name = serializers.CharField(max_length=400)
#     date_of_birth = serializers.DateField()


# todo using model serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class BookSerializer(serializers.ModelSerializer):
    # todo relationship the brings what is in the class info
    # author = AuthorSerializer()
    # todo the below syntax will bring the author name
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ['title', 'description', 'author']
        # todo  will show  the author id
        # author = AuthorSerializer


class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description']
