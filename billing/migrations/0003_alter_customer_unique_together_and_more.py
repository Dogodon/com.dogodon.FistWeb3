# Generated by Django 5.1.1 on 2025-04-21 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0002_alter_customer_numero_client"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="customer",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="customer",
            name="numero_client",
        ),
    ]
