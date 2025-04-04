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
            name="Membership",
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
                ("slug", models.SlugField(blank=True, null=True)),
                (
                    "membership_type",
                    models.CharField(
                        choices=[
                            ("Extended", "Extended"),
                            ("Advanced", "Advanced"),
                            ("Medium", "Medium"),
                            ("Basic", "Basic"),
                            ("Free", "Free"),
                        ],
                        default="Free",
                        max_length=30,
                    ),
                ),
                ("duration", models.PositiveIntegerField(default=7)),
                (
                    "duration_period",
                    models.CharField(
                        choices=[
                            ("Days", "Days"),
                            ("Week", "Week"),
                            ("Months", "Months"),
                        ],
                        default="Day",
                        max_length=100,
                    ),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PayHistory",
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
                    "paystack_charge_id",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                (
                    "paystack_access_code",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("paid", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_for",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="subscription.membership",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserMembership",
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
                    "reference_code",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                (
                    "membership",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_membership",
                        to="subscription.membership",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_membership",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
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
                ("expires_in", models.DateField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "user_membership",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription",
                        to="subscription.usermembership",
                    ),
                ),
            ],
        ),
    ]
