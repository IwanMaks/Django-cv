# Generated by Django 3.1.4 on 2020-12-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfName', models.CharField(max_length=150, verbose_name='Имя')),
                ('title', models.CharField(max_length=150, verbose_name='Приветствие')),
                ('text', models.TextField(max_length=250, verbose_name='Описание себя')),
                ('quote', models.CharField(max_length=150, verbose_name='Цитата')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'О себе',
                'verbose_name_plural': 'О себе',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адресс')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('phone', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('facebook', models.CharField(blank=True, max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=100, verbose_name='Twitter')),
                ('inst', models.CharField(blank=True, max_length=100, verbose_name='Instagram')),
                ('vk', models.CharField(blank=True, max_length=100, verbose_name='ВКонтакте')),
                ('github', models.CharField(blank=True, max_length=100, verbose_name='GitHub')),
                ('youtube', models.CharField(blank=True, max_length=100, verbose_name='YouTube')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50, verbose_name='Название иконки')),
                ('title', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('content', models.TextField(max_length=200, verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Услуга(у)',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название навыка')),
                ('percent', models.IntegerField(verbose_name='Владение в процентах')),
            ],
            options={
                'verbose_name': 'Способность',
                'verbose_name_plural': 'Способности',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год начала работы')),
                ('job', models.CharField(max_length=100, verbose_name='Место работы')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
                ('content', models.TextField(max_length=255, verbose_name='Описание работы')),
            ],
            options={
                'verbose_name': 'Работа(у)',
                'verbose_name_plural': 'Места работы',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
