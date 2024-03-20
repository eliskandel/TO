from django.urls import path 
from .views import read_todo
urlpatterns = [
     path('',read_todo)
]
