# Generated by Django 5.0.6 on 2024-06-23 23:02

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('company', models.CharField(max_length=100, verbose_name='Учебное заведение')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание курса')),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='Дата начала')),
                ('date_end', models.DateField(auto_now=True, null=True, verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('vacancy_title', models.CharField(max_length=100, verbose_name='Название вакансии')),
                ('company', models.CharField(max_length=100, verbose_name='Компания')),
                ('responsibilities', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Обязанности')),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='Дата начала')),
                ('date_end', models.DateField(auto_now=True, null=True, verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работы',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=100, verbose_name='Название стека')),
            ],
            options={
                'verbose_name': 'Стек',
                'verbose_name_plural': 'Стеки',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('min_salary', models.IntegerField(blank=True, null=True, verbose_name='Минимальная зарплата')),
                ('max_salary', models.IntegerField(blank=True, null=True, verbose_name='Максимальная зарплата,')),
                ('about', django_ckeditor_5.fields.CKEditor5Field(verbose_name='О себе')),
                ('github_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на GitHub')),
                ('avatar', models.ImageField(null=True, upload_to='portfolio/resumes', verbose_name='Аватар резюме')),
                ('course', models.ManyToManyField(blank=True, to='portfolio.course', verbose_name='Курсы')),
                ('experience', models.ManyToManyField(blank=True, to='portfolio.experience', verbose_name='Опыт работы')),
                ('skill', models.ManyToManyField(blank=True, to='portfolio.skill', verbose_name='Навыки')),
                ('stack', models.ManyToManyField(blank=True, to='portfolio.stack', verbose_name='Стек')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание проекта')),
                ('avatar', models.ImageField(null=True, upload_to='portfolio/projects', verbose_name='Аватар проекта')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка на проект')),
                ('stack', models.ManyToManyField(to='portfolio.stack', verbose_name='Стеки проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]