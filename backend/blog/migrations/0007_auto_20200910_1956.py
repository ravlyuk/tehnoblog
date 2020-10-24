# Generated by Django 3.1.1 on 2020-09-10 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='comments', to='blog.article', verbose_name='Статья'),
        ),
    ]
