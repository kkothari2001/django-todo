from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {"todo_list": todo_list})


def delete(request, pk):
    todo_deleted = Todo.objects.get(id=pk)
    todo_deleted.delete()
    return redirect('/')
