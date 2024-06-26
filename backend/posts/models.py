from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from portfolio.models import Stack


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    content = CKEditor5Field(
        verbose_name="Описание статьи", config_name="extends")
    stacks = models.ManyToManyField(
        Stack, verbose_name='Стеки', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'Статья: {self.title}'