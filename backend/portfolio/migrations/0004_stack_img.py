# Generated by Django 5.0.6 on 2024-06-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_experience_date_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='img',
            field=models.ImageField(null=True, upload_to='portfolio/stacks', verbose_name='Аватар стека'),
        ),
    ]
