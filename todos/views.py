from django.shortcuts import render, HttpResponse

# Create your views here.

def list_todo_items(request):
    return render(request, 'todos/todo_list.html')
