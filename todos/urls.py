from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_todo_items, name='list')
]