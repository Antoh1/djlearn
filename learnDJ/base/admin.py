from django.contrib import admin
from .models import Author, TodoList, Item

# Register your models here.

admin.site.register(Author)
admin.site.register(TodoList)
admin.site.register(Item)
