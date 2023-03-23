from django.urls import path

from api import views

urlpatterns = [
    path('books', views.books_list),
    path('books/<int:pk>', views.books_detail),
    path('authors', views.author_list)
    # path('books', views.BookListView.as_view())
]
