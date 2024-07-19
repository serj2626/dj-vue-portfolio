from pyexpat import model
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    company = models.CharField(
        max_length=100, verbose_name="Учебное заведение")
    description = CKEditor5Field(
        verbose_name="Описание курса", config_name="extends")
    img = models.ImageField(upload_to="portfolio/courses",
                            null=True, verbose_name="Аватар курса")
    date_start = models.DateField(null=True, verbose_name="Дата начала")
    date_end = models.DateField(null=True, verbose_name="Дата окончания")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"Курс: {self.title}"


class Experience(models.Model):
    vacancy_title = models.CharField(
        max_length=100, verbose_name="Название вакансии")
    company = models.CharField(max_length=100, verbose_name="Компания")
    responsibilities = CKEditor5Field(
        verbose_name="Обязанности", config_name="extends")
    date_start = models.DateField(null=True, verbose_name="Дата начала")
    date_end = models.DateField(
        verbose_name="Дата окончания", null=True)

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

    def __str__(self):
        return f"Опыт работы: {self.vacancy_title}"


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title


class Stack(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название стека")
    img = models.ImageField(
        upload_to="portfolio/stacks", null=True, blank=True, verbose_name="Аватар стека"
    )
    queue = models.SmallIntegerField(verbose_name="Порядок", null=True)
    level = models.SmallIntegerField(
        verbose_name="Уровень владения стеком", null=True)
    slug = models.SlugField(max_length=100, null=True,
                            unique=True, verbose_name="слаг")

    class Meta:
        verbose_name = "Стек"
        verbose_name_plural = "Стеки"
        ordering = ["queue"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название проекта")
    description = CKEditor5Field(
        verbose_name="Описание проекта", config_name="extends")
    stack = models.ManyToManyField(Stack, verbose_name="Стеки проекта")
    avatar = models.ImageField(
        upload_to="portfolio/projects", null=True, verbose_name="Аватар проекта"
    )
    url = models.URLField(verbose_name="Ссылка на проект",
                          null=True, blank=True)

    slug = models.SlugField(max_length=100, null=True,
                            unique=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"Проект {self.title}"


class Resume(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")
    phone = models.CharField(
        max_length=100, default='8-953-160-53-84', verbose_name="Телефон")
    email = models.EmailField(
        max_length=100, default='serj2626@mail.ru', verbose_name="Email")
    country = models.CharField(
        max_length=100, default="Россия", verbose_name="Страна")
    city = models.CharField(
        max_length=100, default="Санкт-Петербург", verbose_name="Город")
    about = CKEditor5Field(verbose_name="О себе", config_name="extends")
    github_url = models.URLField(
        verbose_name="Ссылка на GitHub", null=True, blank=True)
    avatar = models.ImageField(
        upload_to="portfolio/resumes", null=True, verbose_name="Аватар резюме"
    )

    def get_avatar(self):
        if self.avatar:
            return "http://127.0.0.1:8000" + self.avatar.url
        else:
            return ""

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"

    def __str__(self):
        return f"Резюме {self.position}"
