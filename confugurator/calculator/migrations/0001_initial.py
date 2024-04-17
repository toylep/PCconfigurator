# Generated by Django 5.0.4 on 2024-04-16 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("cpu", models.FloatField()),
                ("gpu", models.FloatField()),
                ("motherboard", models.FloatField()),
                ("ram", models.FloatField()),
                ("power_unit", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="CPU",
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
                ("name", models.CharField(max_length=100)),
                ("cost", models.FloatField()),
                ("frequency", models.CharField(max_length=100)),
                ("frequency_of_memory", models.IntegerField()),
                ("tdp", models.IntegerField()),
                ("socket", models.IntegerField()),
                ("is_graphics", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="GPU",
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
                ("name", models.CharField(max_length=100)),
                ("cost", models.FloatField()),
                ("memory", models.IntegerField()),
                ("bar", models.IntegerField()),
                ("frequency", models.IntegerField()),
                ("tdp", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="MotherBoard",
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
                ("name", models.CharField(max_length=100)),
                ("cost", models.FloatField()),
                ("socket", models.IntegerField()),
                ("power_phases", models.IntegerField()),
                ("type_of_memory", models.CharField(max_length=100)),
                ("chipset", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="PowerUnit",
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
                ("name", models.CharField(max_length=100)),
                ("cost", models.FloatField()),
                ("power", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RAM",
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
                ("name", models.CharField(max_length=100)),
                ("cost", models.FloatField()),
                ("value_gb", models.IntegerField()),
                ("type", models.CharField(max_length=100)),
                ("frequency", models.IntegerField()),
                ("is_game", models.BooleanField()),
                ("count", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Configuration",
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
                    "cpu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="calculator.cpu"
                    ),
                ),
                (
                    "gpu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="calculator.gpu"
                    ),
                ),
                (
                    "motherboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.motherboard",
                    ),
                ),
                (
                    "power_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="calculator.powerunit",
                    ),
                ),
                (
                    "ram",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="calculator.ram"
                    ),
                ),
            ],
        ),
    ]