from cgitb import text
from distutils.text_file import TextFile
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Entry(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=500)
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name