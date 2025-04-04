# Generated by Django 5.1.1 on 2025-04-05 04:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                    "customer_type",
                    models.CharField(
                        choices=[
                            ("particulier", "Particulier"),
                            ("professionnel", "Professionnel"),
                        ],
                        default="particulier",
                        max_length=20,
                    ),
                ),
                ("civilite", models.CharField(blank=True, max_length=10, null=True)),
                ("nom", models.CharField(max_length=132)),
                ("prenom", models.CharField(blank=True, max_length=132, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Féminin")],
                        default="M",
                        max_length=1,
                    ),
                ),
                ("telephone", models.CharField(blank=True, max_length=20, null=True)),
                ("adresse", models.CharField(blank=True, max_length=255, null=True)),
                ("code_postal", models.CharField(blank=True, max_length=16, null=True)),
                ("ville", models.CharField(blank=True, max_length=50, null=True)),
                ("pays", models.CharField(blank=True, max_length=50, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "raison_sociale",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "siret",
                    models.PositiveIntegerField(blank=True, null=True, unique=True),
                ),
                (
                    "num_tva_intracom",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("fax", models.CharField(blank=True, max_length=20, null=True)),
                ("fonction", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "telephone_mobile",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "telephone_fixe",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "save_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
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
                ("invoice_date_time", models.DateTimeField(auto_now_add=True)),
                ("total", models.DecimalField(decimal_places=2, max_digits=20)),
                ("last_updated_date", models.DateTimeField(blank=True, null=True)),
                ("paid", models.BooleanField(default=False)),
                (
                    "invoice_type",
                    models.CharField(
                        choices=[
                            ("R", "RECEIPT"),
                            ("P", "PROFORMA INVOICE"),
                            ("I", "INVOICE"),
                        ],
                        max_length=1,
                    ),
                ),
                ("comments", models.TextField(blank=True, max_length=1000, null=True)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="invoices/logos/"
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="billing.customer",
                    ),
                ),
                (
                    "save_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Invoice",
                "verbose_name_plural": "Invoices",
            },
        ),
        migrations.CreateModel(
            name="Article",
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
                    "designation",
                    models.CharField(default="Article Inconnu", max_length=255),
                ),
                ("quantity", models.IntegerField()),
                ("unite", models.CharField(blank=True, max_length=50, null=True)),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "remise",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("tva", models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                (
                    "montant_ht",
                    models.DecimalField(decimal_places=2, default=0, max_digits=20),
                ),
                ("reference", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "famille",
                    models.CharField(
                        choices=[("produit", "Produit"), ("service", "Service")],
                        max_length=50,
                    ),
                ),
                (
                    "prix_achat_ht",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=20, null=True
                    ),
                ),
                (
                    "taux_marge",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "img",
                    models.ImageField(
                        blank=True, null=True, upload_to="articles/imgs/"
                    ),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billing.invoice",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
