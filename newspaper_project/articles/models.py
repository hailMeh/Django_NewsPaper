from django.db import models
from django.contrib.auth import get_user_model  # Берётся авторизованный пользователь
from django.urls import reverse


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, help_text='Введите название сообщения', verbose_name='Название')
    body = models.TextField(help_text='Введите содержание сообщения', verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')  # автодобавление даты в создание сообщения
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Автор')  # Many-To-One в первом параметре -

    # - Передается авторизованный пользователь

    def __str__(self):
        return self.title  # для отображения в админке тайтла

    def get_absolute_url(self):
        return reverse('article_details',
                       args=[str(self.id)])  # Редирект при создании сообщения на шаблон первого параметра


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE,
                                related_name='comments', )  # Много комментариев к одной новости...
    # ...related_name для удобного отображения в шаблоне через for
    comment = models.CharField(max_length=150, )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Автор')  # Many-To-One в первом параметре -

    # - Передается авторизованный пользователь

    def __str__(self):
        return self.comment  # для отображения в админке коммента

    def get_absolute_url(self):
        return reverse('article_list')
