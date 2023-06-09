# Generated by Django 4.1.7 on 2023-05-29 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_tag_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="comments", to="main.tag"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="main.tag"
            ),
        ),
    ]
