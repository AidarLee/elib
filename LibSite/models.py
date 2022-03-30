from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

#my models

class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=200)

    #Utility Variable
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
  

class Recruitment(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(default='SOME TEXT')
    author = models.ManyToManyField(User)
    geeks_field = models.EmailField(max_length = 254)
    theme = models.CharField(max_length=50)
    massage = models.TextField(default='Some Text')

class Video(models.Model):
    name= models.CharField(max_length=500)
    file= models.FileField(upload_to='videos/', null=True, verbose_name="")





class Comment(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



class UploadFile(models.Model):
    title = models.CharField(max_length=255, verbose_name = "Название файла", null=True)
    file = models.FileField(upload_to='documents')

    def __str__(self):
        return self.title





class Notes(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    discription = models.TextField(max_length = 255, verbose_name='Описание', null = True)
    text = models.TextField(verbose_name='Текст')
    created_on = models.DateTimeField(auto_now_add=False, verbose_name='Дата публикации')
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='documents')
 
    def __str__(self):
        verbose_name = ('Запись')
        verbose_name_plural = ('Записи')
        return self.title



