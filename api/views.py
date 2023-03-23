import http

from django.shortcuts import render
from rest_framework.response import Response

from books.models import Book, Author
from .serializers import BookSerializer, BookCreateSerializer, BookUpdateSerializer, AuthorSerializer
from rest_framework.decorators import api_view


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
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         queryset = Author.objects.all()
#         serializers = AuthorSerializer(queryset, many=True)
#         return Response(serializers.data)
