# Generated by Django 3.1.4 on 2020-12-28 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvApp', '0004_auto_20201228_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='pic',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Большая картинка'),
        ),
    ]
