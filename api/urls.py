from django.urls import path

from api import views

urlpatterns = [
    # path('books', views.books_list),
    path('authors/', views.GetAllAuthor.as_view()),
    path("author_create/", views.AuthorCreate.as_view()),
    path('authors/<int:pk>', views.GetAuthor.as_view()),
    path("author_delete/<int:pk>", views.AuthorDeleteView.as_view()),

    path('all/', views.BookCreateView.as_view()),
    path('books/<int:pk>', views.GetBook.as_view()),
    path("book_delete/<int:pk>", views.BookDeleteView.as_view()),



    path('books/', views.BookListView.as_view())
    # path('books', views.BookListView.as_view())
]
