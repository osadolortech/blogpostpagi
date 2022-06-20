from turtle import title
from django.db import models
from django.forms import DateField

# Create your models here.
class BlogpostList(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    created_date = models.DateField(auto_now_add=True)