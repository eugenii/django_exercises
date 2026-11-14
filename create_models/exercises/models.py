from django.db import models

# Create your models here.

class Book(models.Model):
    """Модель учебника с характеристиками."""

    title = models.CharField(max_length=200, verbose_name='Название')

    subject = models.CharField(max_length=200, verbose_name='Предмет', default='Физика')

    description = models.TextField(verbose_name="Аннотация", blank=True, null=True)

    grade = models.PositiveIntegerField(verbose_name='Класс', default=9)

    is_digital = models.BooleanField(verbose_name='Электронное издание', default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', blank=True, null=True)

    class Meta:
        verbose_name = 'учебник'
        verbose_name_plural = 'Учебники'
        ordering = ['-created_at']

    def __str__(self):
        return self.title[:30]


class Author(models.Model):
    """Модель автора."""

    name = models.CharField(max_length=100, verbose_name='Имя автора')

    class Meta:
        verbose_name ='автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name