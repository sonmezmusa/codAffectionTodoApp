from django.urls import path
from .views import *

urlpatterns = [
    path('list/', list_todo_items, name='list'),
    path('insert_todo/', insert_todo_item, name='insert_todo_item'),
]