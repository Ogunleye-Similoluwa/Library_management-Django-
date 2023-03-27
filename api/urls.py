from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from api import views

router = SimpleRouter()
router2 = SimpleRouter()
router.register('authors', views.AuthorViewSet)
router2.register('books', views.BookViewSet)
urlpatterns = [
    # path('book', views.books_list),
    # path('authors/', views.GetAllAuthor.as_view()),
    # path("author_create/", views.AuthorCreate.as_view()),
    # path('author/<int:pk>', views.GetAuthor.as_view()),
    path('authors/<int:pk>', views.author_detail, name="author_detail"),
    # path("author_delete/<int:pk>", views.AuthorDeleteView.as_view()),
    path('', include(router.urls)),

    # path('all/', views.BookView.as_view()),
    # path('create_book/', views.BookCreateView.as_view()),
    # path('book/<int:pk>', views.GetBook.as_view()),
    # path("book_delete/<int:pk>", views.BookDeleteView.as_view()),
    # path('book/', views.BookListView.as_view()),

    path('', include(router2.urls))
    # path('book', views.BookListView.as_view())
]
