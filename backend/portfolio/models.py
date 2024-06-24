from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса')
    company = models.CharField(
        max_length=100, verbose_name='Учебное заведение')
    description = CKEditor5Field(
        verbose_name="Описание курса", config_name="extends")
    date_start = models.DateField(
        auto_now_add=True, verbose_name='Дата начала')
    date_end = models.DateField(auto_now=True,
                                verbose_name='Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'Курс: {self.title}'


class Experience(models.Model):
    vacancy_title = models.CharField(
        max_length=100, verbose_name='Название вакансии')
    company = models.CharField(max_length=100, verbose_name='Компания')
    responsibilities = CKEditor5Field(
        verbose_name="Обязанности", config_name="extends")
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(
        verbose_name='Дата окончания', null=True, blank=True)

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        return f'Опыт работы: {self.vacancy_title}'


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title


class Stack(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название стека')
    img = models.ImageField(upload_to='portfolio/stacks',
                            null=True, verbose_name='Аватар стека')
    slug = models.SlugField(max_length=100, null=True,
                            unique=True, verbose_name='слаг')

    class Meta:
        verbose_name = 'Стек'
        verbose_name_plural = 'Стеки'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    description = CKEditor5Field(
        verbose_name="Описание проекта", config_name="extends")
    stack = models.ManyToManyField(Stack, verbose_name='Стеки проекта')
    avatar = models.ImageField(
        upload_to='portfolio/projects', null=True, verbose_name='Аватар проекта')
    url = models.URLField(verbose_name='Ссылка на проект',
                          null=True, blank=True)

    slug = models.SlugField(max_length=100, null=True,
                            unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'Проект {self.title}'


class Resume(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    position = models.CharField(max_length=100, verbose_name='Должность')
    stack = models.ManyToManyField(
        Stack, verbose_name='Стек', blank=True)
    skill = models.ManyToManyField(
        Skill, verbose_name='Навыки', blank=True)
    course = models.ManyToManyField(
        Course, verbose_name='Курсы', blank=True)
    experience = models.ManyToManyField(
        Experience, verbose_name='Опыт работы', blank=True)
    min_salary = models.IntegerField(
        verbose_name='Минимальная зарплата', blank=True, null=True)
    max_salary = models.IntegerField(
        verbose_name='Максимальная зарплата,', blank=True, null=True)
    about = CKEditor5Field(
        verbose_name="О себе", config_name="extends")
    github_url = models.URLField(
        verbose_name='Ссылка на GitHub', null=True, blank=True)
    avatar = models.ImageField(
        upload_to='portfolio/resumes', null=True, verbose_name='Аватар резюме')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'Резюме {self.position}'
