# Generated by Django 5.0.6 on 2024-10-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_created_at_alter_blog_preview"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Признак публикации"),
        ),
        migrations.AddField(
            model_name="blog",
            name="slug",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="slug"
            ),
        ),
        migrations.AddField(
            model_name="blog",
            name="views_count",
            field=models.IntegerField(default=0, verbose_name="Просмотры"),
        ),
    ]
