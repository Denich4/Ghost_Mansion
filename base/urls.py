from django.contrib import admin
from django.urls import path
from base.views import index

urlpatterns = [
    path('', index, name='index'),
]
