from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name