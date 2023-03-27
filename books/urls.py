from django.urls import path
from books.views import BookCreateView

urlpatterns = [
    path('view/', BookCreateView.as_view(), name='create'),
]
