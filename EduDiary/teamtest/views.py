from django.http import HttpResponse
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

def welcome(request):
    return HttpResponse("<h1>Добро пожаловать на EduDiary!</h1>")


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
