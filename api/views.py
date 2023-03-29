import http

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.models import Book, Author, BookInstance
from .pagination import DefaultPageNumberPagination
from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer, BookCreateSerializer, BookUpdateSerializer, AuthorSerializer, BookInstanceSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookCreateSerializer


class BookView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = "pk"
    serializer_class = BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GetBook(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class GetAllAuthor(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GetAuthor(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "pk"


class AuthorCreate(generics.CreateAPIView):
    serializer_class = AuthorSerializer


class AuthorDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    lookup_field = "pk"
    serializer_class = AuthorSerializer


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInstanceViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


# @api_view(['GET', 'POST'])
# def books_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.all()
#         serializers = BookSerializer(queryset, many=True)
#         return Response(serializers.data,http.HTTPStatus.OK)
#     elif request.method == "POST":
#         book = BookCreateSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("Book saved successfully")
#
#
# @api_view(['GET','PUT', 'DELETE'])
# def books_detail(request, pk):
#     if request.method == "PUT":
#         queryset = Book.objects.get(id=pk)
#         book = BookUpdateSerializer(queryset, data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("Book updated successfully" )
#     elif request.method == "DELETE":
#         book = Book.objects.get(id=pk)
#         book.delete()
#         return Response("Book Deleted successfully")
#
#
@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        queryset = Author.objects.all()
        serializers = AuthorSerializer(queryset, many=True)
        return Response(serializers.data)
