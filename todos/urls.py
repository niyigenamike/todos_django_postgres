# todos/urls.py
from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('list/', views.list_todo_items, name='todo_list'),
    path('insert/', views.insert_todo_item, name='insert_todo_item'),
    path('complete/<int:pk>/', views.complete_todo_item, name='complete_todo_item'),  # Fixed
    path('delete/<int:pk>/', views.delete_todo_item, name='delete_todo_item'),  # Fixed
]