# Generated by Django 5.0.6 on 2024-06-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_stack_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stack',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/stacks', verbose_name='Аватар стека'),
        ),
    ]
