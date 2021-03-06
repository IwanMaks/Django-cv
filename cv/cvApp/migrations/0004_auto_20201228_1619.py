# Generated by Django 3.1.4 on 2020-12-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvApp', '0003_auto_20201227_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.CharField(blank=True, max_length=150, verbose_name='Категория разработки'),
        ),
        migrations.AddField(
            model_name='work',
            name='client',
            field=models.CharField(blank=True, help_text='Если клмента не было, то поставте прочерк', max_length=100, verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='work',
            name='date',
            field=models.DateTimeField(blank=True, default='2000-07-12 12:33', verbose_name='Дата окончания разработки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание проекта'),
        ),
        migrations.AddField(
            model_name='work',
            name='liveurl',
            field=models.CharField(blank=True, help_text='Если ссылка отсутсвует, то поставьте прочерк', max_length=255, verbose_name='Рабочая ссылка на проект'),
        ),
        migrations.AddField(
            model_name='work',
            name='skill',
            field=models.CharField(blank=True, help_text='Перечислите технологии через запятую', max_length=255, verbose_name='Технологии, которые применялись'),
        ),
        migrations.AddField(
            model_name='work',
            name='title',
            field=models.CharField(default=1, max_length=200, verbose_name='Название проекта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='quote',
            field=models.TextField(max_length=150, verbose_name='Цитата'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.TextField(max_length=150, verbose_name='Приветствие'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Мини фото'),
        ),
    ]
