# Generated by Django 5.0.3 on 2024-03-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MouseEvent",
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
                (
                    "event_type",
                    models.CharField(
                        choices=[("click", "Click"), ("move", "Move")], max_length=5
                    ),
                ),
                ("x", models.IntegerField()),
                ("y", models.IntegerField()),
                ("timestamp", models.DateTimeField()),
            ],
        ),
    ]
