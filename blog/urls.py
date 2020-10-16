from django.urls import path, include
from .views import *
urlpatterns = [
    path('', homepage, name='homepage'),
    path('posts/', PostsList.as_view(), name='posts_list'),


]
