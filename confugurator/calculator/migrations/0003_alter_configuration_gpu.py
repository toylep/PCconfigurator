# Generated by Django 5.0.4 on 2024-04-17 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "calculator",
            "0002_alter_cpu_frequency_alter_cpu_frequency_of_memory_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="configuration",
            name="gpu",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calculator.gpu",
            ),
        ),
    ]
