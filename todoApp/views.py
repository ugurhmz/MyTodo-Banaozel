from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class IndexView(ListView):
    template_name ='posts/index.html'
    model = PostTodo