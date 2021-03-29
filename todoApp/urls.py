from django.urls import path
from .views import *



urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('create/',todo_ekle, name='create' ),
]