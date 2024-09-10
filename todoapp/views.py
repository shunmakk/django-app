from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from todoapp.models import Task
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
# def taskList(request):
#     return HttpResponse("<h1>Django</h1>")

class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(CreateView):
    model = Task
    # 全てのモデル
    fields =  "__all__"
    success_url = reverse_lazy("tasks")
