# Generated by Django 3.1.1 on 2020-09-08 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Название'),
        ),
    ]
