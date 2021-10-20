from django.shortcuts import render
from rest_framework.response import Response
from .models import User 
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import CrateUserSerializer, UserSerializer
from rest_framework import parsers
from django_filters import rest_framework as filters
from rest_framework import permissions
from django.http import HttpResponse
import json
from django.core.mail import send_mail


# Create your views here.


class UserFilter(filters.FilterSet):
    

    class Meta:
        model = User
        fields =['gender', 'last_name', 'first_name']
class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter


class CreateUserView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser , parsers.MultiPartParser)
    queryset = User.objects.all()
    serializer_class = CrateUserSerializer


class UserLikeView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request, pk, format=None):
        user_to_like = User.objects.get(id=pk)
        user_to_like.likes.add(request.user.id)
       
        if user_to_like in request.user.likes.all():
            send_mail(
                    'Взаимная симпатия',
                    'Вы понравились '+" " + str(user_to_like.first_name) + " " +'Почта участника: '+ str(user_to_like.email),
                    'testanisapptrix18@yandex.ru',
                    [request.user.email],
                    fail_silently=True,
                )
        
        return  HttpResponse(json.dumps({'message': "user liked"}))

    

   