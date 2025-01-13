# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from .models import Todo, Category
from .forms import TodoForm

def list_todo_items(request):
    context = {
        'todo_list': Todo.objects.active(),
        'completed_list': Todo.objects.completed(),
        'categories': Category.objects.all()
    }
    return render(request, 'todos/todo_list.html', context)

@transaction.atomic
def insert_todo_item(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            messages.success(request, 'Todo added successfully!')
            return redirect('todo_list')
        else:
            messages.error(request, 'Error adding todo!')
    return redirect('todo_list')

def complete_todo_item(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.mark_as_completed()
    messages.success(request, 'Todo marked as completed!')
    return redirect('todo_list')

def delete_todo_item(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')