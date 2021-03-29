from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import *
from .models import *


#_________________________________ IndexView _____________________________________
class IndexView(ListView):
    template_name ='posts/index.html'
    model = PostTodo
    context_object_name = 'posts'

    def get_queryset(self):

        return PostTodo.objects.all().order_by('-id')


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

@login_required(login_url='/')
def todo_ekle(request):
    form = TodoCreatForm(request.POST or None, files= request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        form.save_m2m()
        messages.success(request,"Başarılı eklendi..")

        return redirect('detay',slug=post.slug)

    context = {
        'form':form,
    }


    return render(request,"posts/todo-ekle.html", context= context)


#_________________________________ todo_guncelle _____________________________________
@login_required(login_url='/')
def todo_guncelle(request,slug):

        post = get_object_or_404(PostTodo, slug=slug, user = request.user)
        form = TodoUpdateForm(request.POST or None, files=request.FILES or None, instance=post)

        if form.is_valid():
             form.save()
             messages.success(request,"Form Başarıyla Güncellendi")
             return redirect('index')


        context = {
            'form':form,
        }


        return render(request,"posts/todo-guncelle.html",context=context)



#_________________________________ todo_sil _____________________________________

@login_required(login_url='/')
def todo_sil(request,slug):
    get_object_or_404(PostTodo, slug=slug, user=request.user).delete()
    messages.warning(request,"Kurs Başarıyla silindi")


    return redirect("index")



#_________________________________ biten_todolar _____________________________________

class BitenTodo(ListView):
    template_name = 'posts/biten-todos.html'
    model = PostTodo
    context_object_name = 'bitenposts'  #key ->value gibi düşünebilirsin.

    def get_queryset(self):

        return PostTodo.objects.filter(isFinished=True).order_by('-id')



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BitenTodo,self).get_context_data(**kwargs)
        context['isFinished'] = PostTodo.objects.all().filter(isFinished=True)

        return context




def yes_finish(request, slug):
    todo = PostTodo.objects.get(slug=slug)
    todo.isFinished = True
    todo.save()
    return redirect("index")