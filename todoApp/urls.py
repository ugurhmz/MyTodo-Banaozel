from django.urls import path
from .views import *



urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('detay/<slug:slug>',post_detail , name='detay'),
    path('create/',todo_ekle, name='create' ),
]