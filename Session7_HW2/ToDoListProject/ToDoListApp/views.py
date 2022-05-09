from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# Create your views here.
def home(request):
    todo_list = Todo.objects.all().order_by('deadline')

    for todo in todo_list:
        date_diff = todo.deadline - datetime.date(datetime.now())
        todo.remain = date_diff.days

    return render(request, 'home.html', { 'todo_list' : todo_list })


def new(request):
    if request.method == 'POST':
        todo = Todo.objects.create(
            title = request.POST['title'],
            deadline = request.POST['deadline'],
            content = request.POST['content']
        )
        return redirect('detail', todo.pk)
    
    return render(request, 'new.html')


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    return render(request, 'detail.html', { 'todo' : todo })


def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if request.method == 'POST':
        Todo.objects.filter(pk=todo_pk).update(
            title = request.POST['title'],
            deadline = request.POST['deadline'],
            content = request.POST['content']
        )
        return redirect('detail', todo_pk)
    
    return render(request, 'edit.html', { 'todo' : todo })


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect('home')