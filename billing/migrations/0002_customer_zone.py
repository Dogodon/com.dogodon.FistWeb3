# Generated by Django 5.1.1 on 2025-04-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="zone",
            field=models.CharField(
                choices=[("rurale", "rurale"), ("urbaine", "urbaine")],
                default="RURALE",
                max_length=10,
            ),
        ),
    ]
