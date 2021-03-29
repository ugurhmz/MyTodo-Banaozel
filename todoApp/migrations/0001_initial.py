# Generated by Django 3.1.7 on 2021-03-29 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('publishing_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='resimler/default_img.jpg', null=True, upload_to='resimler/')),
                ('slug', models.SlugField(default='slug', editable=False)),
                ('isFinished', models.BooleanField(default=False)),
                ('educationTime', models.PositiveIntegerField(default=0)),
                ('countFinished', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]