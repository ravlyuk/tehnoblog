# Generated by Django 3.1.1 on 2020-10-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_remove_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(default='article/default/750x300.png', upload_to='article/', verbose_name='Изображение'),
        ),
    ]
