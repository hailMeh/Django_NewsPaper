from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model  # Будет использоваться в поле Автора поста
from django.urls import reverse


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, help_text='Введите название сообщения', verbose_name='Название')
    body = models.TextField(help_text='Введите содержание сообщения', verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')  # Значение по умолчанию из settings
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Автор')  # Считывается залогиненный автор

    def __str__(self):
        return self.title  # для отображения в админке тайтла

    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments',)  # Много комментариев к одной новости
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               )  # Считывается залогиненный автор

    def __str__(self):
        return self.comment  # для отображения в админке коммента


    def get_absolute_url(self):
        return reverse('article_list')
