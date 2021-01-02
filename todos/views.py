from django.shortcuts import render, redirect
from django.http import  HttpResponse, HttpRequest
from .models import *

# Create your views here.

def list_todo_items(request):
    todo_list = Todo.objects.all()

    context = {
        'todo_list' : todo_list
    }

    return render(request, 'todos/todo_list.html', context)


def insert_todo_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')