from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60, verbose_name="Имя")
    email = models.EmailField(max_length=60, verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
