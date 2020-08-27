# Generated by Django 3.1 on 2020-08-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('photo_link1', models.URLField(verbose_name='Ссылка на фото 1')),
                ('photo_link2', models.URLField(blank=True, verbose_name='Ссылка на фото 2')),
                ('photo_link3', models.URLField(blank=True, verbose_name='Ссылка на фото 3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
    ]
