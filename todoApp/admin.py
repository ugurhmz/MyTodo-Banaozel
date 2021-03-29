from django.contrib import admin
from todoApp.models import PostTodo


@admin.register(PostTodo)
class PostTodoAdmin(admin.ModelAdmin):
        list_filter = ['publishing_date']
        list_display = ['title','publishing_date','user','isFinished','educationTime']
        search_fields = ['title','publishing_date']


        class Meta:
            model = PostTodo
