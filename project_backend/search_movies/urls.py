from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.searching_data, name='searching_data'),
    path('<str:imdb>/', views.youtubeTrailer, name='youtubeTrailer'),
]
