from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import *
from .models import *
from django.db.models import F
#_________________________________ IndexView _____________________________________
class IndexView(ListView):
    template_name ='posts/index.html'
    model = PostTodo
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)

        return context


#_________________________________ post_detail _____________________________________
def post_detail(request,slug):
    detay = get_object_or_404(PostTodo, slug=slug)


    context = {
        'detay':detay,

    }

    return render(request,"posts/todo-detay.html", context=context)




#_________________________________ todo_ekle _____________________________________

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