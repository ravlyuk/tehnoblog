# Generated by Django 3.1.1 on 2020-10-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201017_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, default='article/default/750x300.png', upload_to='article/', verbose_name='Изображение'),
        ),
    ]
