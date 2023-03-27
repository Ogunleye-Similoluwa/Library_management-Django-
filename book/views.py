from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from book.models import Book, Author


# Create your views here.
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'isbn', 'description']
    template_name = 'create_post.html'



class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    template_name = 'author_list.html'


class AuthorList(ListView):
    model = Author
    template_name = "author.html"
    context_object_name = "author"





