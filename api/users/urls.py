from django.urls import path
from .views import UserListView , CreateUserView 
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
   
    path('create', CreateUserView.as_view()),
    path('list', UserListView.as_view()),
    
   


]




urlpatterns = format_suffix_patterns(urlpatterns)