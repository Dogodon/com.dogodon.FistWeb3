# Generated by Django 5.1.1 on 2025-04-27 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0007_alter_avoir_invoice"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="avoir",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="articles",
                to="billing.avoir",
            ),
        ),
    ]
