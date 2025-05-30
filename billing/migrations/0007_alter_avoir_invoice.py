# Generated by Django 5.1.1 on 2025-04-26 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0006_remove_invoice_facture_liee_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avoir",
            name="invoice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="avoirs",
                to="billing.invoice",
            ),
        ),
    ]
