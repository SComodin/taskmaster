# Generated by Django 4.1.3 on 2022-11-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_rename_order_task_orden_task_color"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=250)),
                ("code", models.SlugField(max_length=4)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
    ]
