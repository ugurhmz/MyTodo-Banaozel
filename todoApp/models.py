from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse


class PostTodo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    sira = models.PositiveIntegerField(default=1)
    publishing_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    image = models.ImageField(null=True, blank=True, upload_to='resimler/', default='resimler/default_img.jpg')
    slug = models.SlugField(default="slug",editable=False)
    isFinished = models.BooleanField(default=False)
    educationTime = models.PositiveIntegerField(default=0)
    countFinished = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    def get_delete_url(self):
        return reverse('todo_sil', kwargs={'slug': self.slug})




    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(PostTodo,self).save(*args,**kwargs)
