# Generated by Django 3.1.1 on 2020-09-13 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200911_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(blank=True, default=0, verbose_name='Понравилось'),
        ),
    ]
