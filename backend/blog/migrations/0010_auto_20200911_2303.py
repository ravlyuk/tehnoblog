# Generated by Django 3.1.1 on 2020-09-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rating_ratingstar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='movie',
            new_name='article',
        ),
    ]
