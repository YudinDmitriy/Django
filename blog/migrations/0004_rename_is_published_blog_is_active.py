# Generated by Django 5.0.6 on 2024-10-02 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_blog_is_published_blog_slug_blog_views_count"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="is_published",
            new_name="is_active",
        ),
    ]
