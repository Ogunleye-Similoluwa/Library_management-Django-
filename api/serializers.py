from abc import ABC

from rest_framework import serializers
from book.models import Book, Author, BookInstance
from djoser.serializers import UserCreateSerializer as CreateSerializer


class BookInstanceSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField

    class Meta:
        model = BookInstance
        fields = ['uniqueId', 'due_date', 'status', 'book', 'imprint', 'borrower']


class UserCreateSerializer(CreateSerializer):
    class Meta(CreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


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


class BookCreateSerializer(serializers.ModelSerializer):
    # returns authors name
    author = serializers.StringRelatedField()
    discount_price = serializers.SerializerMethodField(method_name='discount')

    class Meta:
        model = Book
        fields = ['title', 'description', 'genre', 'language', 'price', 'author', 'discount_price']


class BookSerializer(serializers.ModelSerializer):
    # todo relationship the brings what is in the class info
    # author = AuthorSerializer()
    # todo the below syntax will bring the author name
    # author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['title', 'description', 'genre', 'language', 'price', 'author', 'date_added', 'discount_price']
        # todo links to the route of the view

    author = serializers.HyperlinkedRelatedField(queryset=Author.objects.all(), view_name='author_detail',
                                                 lookup_field="pk")
    discount_price = serializers.SerializerMethodField(method_name='discount')
    date_added = serializers.DateField()

    def discount(self, book: Book):
        return book.price * 25 / 100

    # todo  will show  the author id
    # author = AuthorSerializer


class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description']
