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
import django_filters.rest_framework

from math import radians, degrees, sin, cos, asin, acos, sqrt

# Create your views here.





def calculateDistance(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )
class CustomFilter(django_filters.rest_framework.DjangoFilterBackend):
    def filter_queryset(self, request , queryset,view):
        alluser = queryset
        newQueryset = []
        distparam = request.GET.get('distance')
        if distparam and bool(int(distparam)):
            for user in alluser:
                current_user_long = request.user.longitude
                current_user_lat = request.user.latitude
                alluser_long = user.longitde
                alluser_lat = user.latitude
                distance = calculateDistance(current_user_long, current_user_lat, alluser_long, alluser_lat)
                if distance > distparam:
                    newQueryset.push(user)
            return newQueryset
        return queryset
class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields =['gender', 'last_name', 'first_name' ]
class UserListView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    filter_backends = CustomFilter


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
            send_mail(
                'Взаимная симпатия',
                'Вы понравились '+" " +
                str(request.user.first_name) + " " +
                'Почта участника: ' + str(request.user.email),
                'testanisapptrix18@yandex.ru',
                [user_to_like.email],
                fail_silently=True,
            )
        
        return  HttpResponse(json.dumps({'message': "user liked"}))

    

   
