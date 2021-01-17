from django.db import models
from django.urls import reverse


class About(models.Model):
    selfName = models.CharField(max_length=150, verbose_name='Имя')
    title = models.TextField(max_length=150, verbose_name='Приветствие')
    text = models.TextField(max_length=250, verbose_name='Описание себя')
    quote = models.TextField(max_length=150, verbose_name='Цитата')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return self.selfName

    class Meta:
        verbose_name = 'О себе'
        verbose_name_plural = 'О себе'


class Knowledge(models.Model):
    icon = models.CharField(max_length=50, verbose_name='Название иконки')
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    content = models.TextField(max_length=200, verbose_name='Описание услуги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга(у)'
        verbose_name_plural = 'Услуги'


class Skill(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название навыка')
    percent = models.IntegerField(verbose_name='Владение в процентах')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способность'
        verbose_name_plural = 'Способности'


class Story(models.Model):
    year = models.IntegerField(verbose_name='Год начала работы')
    job = models.CharField(max_length=100, verbose_name='Место работы')
    post = models.CharField(max_length=100, verbose_name='Должность')
    content = models.TextField(max_length=255, verbose_name='Описание работы')

    def __str__(self):
        return self.post

    class Meta:
        ordering = ['-year']
        verbose_name = 'Работа(у)'
        verbose_name_plural = 'Места работы'


class Work(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    image = models.ImageField(verbose_name='Мини фото', upload_to='photos/%Y/%m/%d/')
    pic = models.ImageField(verbose_name='Большая картинка', upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(verbose_name='Описание проекта', blank=True)
    date = models.DateField(verbose_name='Дата окончания разработки', blank=True)
    client = models.CharField(max_length=100, verbose_name='Клиент', help_text='Если клмента не было, то поставте прочерк', blank=True)
    category = models.CharField(max_length=150, verbose_name='Категория разработки', blank=True)
    skill = models.CharField(max_length=255, verbose_name='Технологии, которые применялись', help_text='Перечислите технологии через запятую', blank=True)
    liveurl = models.CharField(max_length=255, verbose_name='Рабочая ссылка на проект', help_text='Если ссылка отсутсвует, то поставьте прочерк', blank=True)


    def get_absolute_url(self):
        return reverse('view_work', kwargs={"pk": self.pk})

    def __str__(self):
        return 'Проект'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Contacts(models.Model):
    address = models.CharField(max_length=100, verbose_name='Адресс', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class SocialLinks(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название соц сети (иконки)')
    link = models.CharField(max_length=255, verbose_name='Ссылка на соц сеть')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка на соц сеть'
        verbose_name_plural = 'Социальные сети'


class AllImg(models.Model):
    startImg = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка для стартовой страницы',
                                 help_text='Размер изображения должен быть 1920х1300')
    skillImg = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка для раздела навыков',
                                 help_text='Размер изображения должен быть 800х1040')
    contactImg = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка для формы обратной связи',
                                   help_text='Размер изображения должен быть 1920х1300')

    def __str__(self):
        return 'Картинки'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Все изображения'
