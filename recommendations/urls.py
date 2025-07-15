from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/', views.recommend, name='recommend'),
    path("delete/<str:movie_id>", views.delete, name="delete"),
    path('fuckoff/', views.fuckoff, name="fuckoff")
]