from django import forms
from .models import PostTodo


class TodoCreatForm(forms.ModelForm):


        class Meta:
            model =PostTodo
            fields = [
                'title',
                'description',
                'image',
                'isFinished',
                'educationTime'
            ]