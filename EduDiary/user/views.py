from rest_framework import generics, renderers
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    renderer_classes = [JSONRenderer]