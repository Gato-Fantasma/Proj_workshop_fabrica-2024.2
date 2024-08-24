from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weather_info = models.JSONField(null=True, blank=True)  # Campo para armazenar dados da API de clima

    def __str__(self):
        return self.title

