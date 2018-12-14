from django.contrib import admin
from django.urls import path, include
from .views import get_users


urlpatterns = [
    path('api/members', get_users)
]
