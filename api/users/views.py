from django.shortcuts import render
from rest_framework.response import Response
from .models import User 
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import CrateUserSerializer, UserSerializer
from rest_framework import parsers


# Create your views here.
class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser , parsers.MultiPartParser)
    queryset = User.objects.all()
    serializer_class = CrateUserSerializer
   