from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import *
from .models import *


class IndexView(ListView):
    template_name ='posts/index.html'
    model = PostTodo
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)

        return context




def todo_ekle(request):
    form = TodoCreatForm(request.POST or None, files= request.FILES or None)

    if form.is_valid():
        post = form.save()
        post.user = request.user
        post.save()
        messages.success(request,"Başarılı eklendi..")

        return redirect('index')

    context = {
        'form':form,
    }


    return render(request,"posts/todo-ekle.html", context= context)