# admin.py
from django.contrib import admin
from .models import Todo, Category

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('content', 'priority', 'is_completed', 'created_at')
    list_filter = ('priority', 'is_completed')
    search_fields = ('content',)

admin.site.register(Category)