# Generated by Django 4.1.7 on 2023-05-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("writer", models.CharField(max_length=100)),
                ("pub_date", models.DateTimeField()),
                ("weather", models.CharField(max_length=50)),
                ("mood", models.CharField(max_length=50)),
                ("body", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="blog/")),
            ],
        ),
    ]
