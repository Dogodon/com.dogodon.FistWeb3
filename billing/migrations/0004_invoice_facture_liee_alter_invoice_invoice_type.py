# Generated by Django 5.1.1 on 2025-04-24 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0003_alter_customer_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="facture_liee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="avoirs",
                to="billing.invoice",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="invoice_type",
            field=models.CharField(
                choices=[
                    ("R", "RECEIPT"),
                    ("P", "PROFORMA INVOICE"),
                    ("I", "INVOICE"),
                    ("A", "AVOIR"),
                ],
                max_length=1,
            ),
        ),
    ]
