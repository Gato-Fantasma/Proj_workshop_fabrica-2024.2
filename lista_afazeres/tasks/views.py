import requests
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, Category

def get_weather(city):
    api_key = '92ab249797b7cbc89ffba9b56c9e7697'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return None

class CategoryListView(ListView):
    model = Category
    template_name = 'tasks/category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'tasks/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'tasks/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'tasks/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'due_date', 'category']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        city = form.cleaned_data.get('city')
        weather_data = get_weather(city)
        form.instance.weather_info = weather_data
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'due_date', 'category']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        city = form.cleaned_data.get('city')
        weather_data = get_weather(city)
        form.instance.weather_info = weather_data
        return super().form_valid(form)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
