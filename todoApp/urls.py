from django.urls import path
from .views import *



urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('detay/<slug:slug>',post_detail , name='detay'),
    path('create/',todo_ekle, name='create' ),
    path('todo-guncelle/<slug:slug>',todo_guncelle, name='todo_guncelle' ),
    path('todo-sil/<slug:slug>',todo_sil, name='todo_sil' ),
    path('biten-todo',BitenTodo.as_view(),name='biten_todo'),
    path('yes_finish/<slug:slug>', yes_finish, name="yes_finish"),
]