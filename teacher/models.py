from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    is_student = models.BooleanField(default=False, name='is_student', verbose_name='Студент?')
    is_teacher = models.BooleanField(default=False, name='is_teacher', verbose_name='Учитель?')
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.crew_password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Дисциплина')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return self.name


class Grade(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    VALUE_CHOICES = [(2, '2'),
                     (3, '3'),
                     (4, '4'),
                     (5, '5')]
    value = models.SmallIntegerField(choices=VALUE_CHOICES, default=None, verbose_name='Оценка', null=True)

    def __str__(self):
        return self.value

