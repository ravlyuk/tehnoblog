# Generated by Django 3.1.1 on 2020-10-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='http://placehold.it/750x300', null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
