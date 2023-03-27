from django.urls import path
from book.views import BookCreateView

urlpatterns = [
    path('view/', BookCreateView.as_view(), name='create'),
]
