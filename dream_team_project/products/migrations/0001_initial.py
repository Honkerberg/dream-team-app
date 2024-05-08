# Generated by Django 5.0.4 on 2024-05-08 11:10

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
                (
                    "category_name",
                    models.CharField(max_length=50, verbose_name="Category Name"),
                ),
                (
                    "category_description",
                    models.TextField(
                        max_length=200, verbose_name="Category Description"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Manufacturer",
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
                    "manufacturer_name",
                    models.CharField(max_length=50, verbose_name="Manufacturer"),
                ),
                (
                    "manufacturer_country",
                    models.CharField(
                        max_length=20, verbose_name="Manufacturer Country"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StockPosition",
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
                    "rack_name",
                    models.CharField(max_length=20, verbose_name="Rack Name"),
                ),
                (
                    "shelf_name",
                    models.CharField(max_length=20, verbose_name="Shelf Name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                    "product_name",
                    models.CharField(max_length=100, verbose_name="Product Name"),
                ),
                (
                    "product_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Product Price"
                    ),
                ),
                (
                    "product_currency",
                    models.CharField(
                        choices=[
                            ("CZK", "Czech crowns"),
                            ("USD", "Dollar"),
                            ("EUR", "Euros"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "product_category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.category",
                    ),
                ),
                (
                    "product_manufacturer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.manufacturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StockInventory",
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
                ("quantity", models.IntegerField(verbose_name="Quantity")),
                (
                    "date_of_acceptance",
                    models.DateField(verbose_name="Date of Acceptance"),
                ),
                (
                    "date_of_manufacture",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of Manufacture"
                    ),
                ),
                (
                    "expiration_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Expiration Date"
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="stock_position_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.stockposition"
            ),
        ),
    ]
