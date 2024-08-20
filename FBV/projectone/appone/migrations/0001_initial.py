# Generated by Django 5.0.6 on 2024-08-14 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="car",
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
                ("engine", models.CharField(max_length=100)),
                ("torque", models.CharField(max_length=100)),
                ("power", models.CharField(max_length=100)),
                ("seating_capacity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="carImage",
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
                ("image", models.ImageField(upload_to="car_images/")),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="imgs",
                        to="appone.car",
                    ),
                ),
            ],
        ),
    ]