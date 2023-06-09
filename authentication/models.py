from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    birthday = models.DateField(blank=False, null=False, default='2023-06-07')
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    date_joined = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)

    def __str__(self):
        return self.username
