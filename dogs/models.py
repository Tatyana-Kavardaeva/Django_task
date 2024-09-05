from django.db import models

from users.models import User


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название породы",
        help_text="Введите название породы",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание породы",
        help_text="Введите описание породы",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода",
        help_text="Введите породу собаки",
        null=True,
        blank=True,
        related_name='dogs',
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
    )
    date_born = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
        help_text="Введите дату рождения",
    )

    view_counter = models.PositiveIntegerField(
        verbose_name="Просмотры",
        help_text="Укажите количество просмотров",
        default=0
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец',
                              help_text='Укажите владельца собаки', blank=True,
                              null=True)

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание собаки",
        help_text="Введите описание собаки",
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]
        permissions = [
            ('can_edit_bread', 'Can edit bread'),
            ('can_edit_description', 'Can edit description')
        ]

    def __str__(self):
        return self.name


class Parent(models.Model):
    dog = models.ForeignKey(
        Dog,
        related_name='parents',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Собака'
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Кличка",
        help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода",
        help_text="Введите породу собаки",
        null=True,
        blank=True,
        related_name='parent_dogs',
    )

    year_born = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Временный год рождения",
        help_text="Временное поле для преобразования года рождения",
    )

    class Meta:
        verbose_name = "Собака родитель"
        verbose_name_plural = "Собаки родители"
        ordering = ["breed", "name"]
        permissions = [
            ('can_edit_bread', 'Can edit bread'),
            ('can_edit_description', 'Can edit description')
        ]

    def __str__(self):
        return self.name


class Test(models.Model):
    title = models.CharField(max_length=150, verbose_name='Статья')
    body = models.TextField(verbose_name='Сообщение')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        permissions = [
            (
                'set_published',
                'Can publish posts'
            )
        ]