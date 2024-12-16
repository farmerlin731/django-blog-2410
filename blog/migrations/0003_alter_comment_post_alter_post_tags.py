# Generated by Django 5.1.3 on 2024-12-16 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blog.post",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(related_name="posts", to="blog.tag"),
        ),
    ]
