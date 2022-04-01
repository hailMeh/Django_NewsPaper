from django.db import models
from django.contrib.auth.models import AbstractUser  # Изменение в стандартную модель юзера

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)  # Добавление нового поля в стандартную модель данных юзера
    hairColor = models.CharField(max_length=50, null=True)
