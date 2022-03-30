from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Notes(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    discription = models.TextField(max_length = 255, verbose_name='Описание', null = True)
    text = models.TextField(verbose_name='Текст')
    created_on = models.DateTimeField(auto_now_add=False, verbose_name='Дата публикации')
 
    def __str__(self):
        verbose_name = ('Запись')
        verbose_name_plural = ('Записи')
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to='Изображение', null = True)
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='Изображения')
