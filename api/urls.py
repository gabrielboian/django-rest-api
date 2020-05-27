from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('animal', AnimalListView.as_view(), name='animal-post'),
    path('animal/<mode>', AnimalListView.as_view(), name='animal-get'),
    path('animal/detail/<id>', AnimalDetails.as_view(), name='animal-id'),
]