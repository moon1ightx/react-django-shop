from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
# Create your views here.

class signUp(CreateAPIView):
    model = User
    serializer_class = UserSerializer