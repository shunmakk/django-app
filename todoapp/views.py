from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from todoapp.models import Task

# Create your views here.
# def taskList(request):
#     return HttpResponse("<h1>Django</h1>")

class TaskList(ListView):
    model = Task