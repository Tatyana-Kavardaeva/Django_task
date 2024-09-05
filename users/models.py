from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True, null=True,
                             help_text='Введите номер телефона')
    tg_name = models.CharField(max_length=50, verbose_name='Ник телеграм', null=True, blank=True,
                               help_text='Введите ник телеграм')
    avatar = models.ImageField(upload_to='users/avatars', null=True, blank=True, verbose_name='Аватар',
                               help_text='Загрузите свой аватар')
    token = models.CharField(max_length=100, verbose_name='токен', blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
