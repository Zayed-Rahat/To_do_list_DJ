# Generated by Django 4.2.3 on 2023-08-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_taskmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100, unique=True)),
        ),
    ]
