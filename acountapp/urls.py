
from django.contrib import admin
from django.urls import path, include

from acountapp.views import hello_world

urlpatterns = [
    path('hello_world/', hello_world, name='hello_word')
]
