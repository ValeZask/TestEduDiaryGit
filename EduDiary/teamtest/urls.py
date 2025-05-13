from django.urls import path
from . import views
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
