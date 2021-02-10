# Generated by Django 3.1.6 on 2021-02-10 10:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("products", "0004_auto_20210210_1120")]

    operations = [
        migrations.RemoveField(model_name="productshop", name="delivery_price"),
        migrations.RemoveField(model_name="productshop", name="price"),
        migrations.AlterField(
            model_name="product",
            name="url_to_scrape_product",
            field=models.CharField(
                max_length=1000, unique=True, verbose_name="Url to scrape product"
            ),
        ),
        migrations.CreateModel(
            name="ParsedProductPrice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "Price cannot be less than 0!"
                            )
                        ],
                        verbose_name="Gross Price",
                    ),
                ),
                (
                    "delivery_price",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "Price cannot be less than 0!"
                            )
                        ],
                        verbose_name="Delivery Price",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="historical_price",
                        to="products.productshop",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Parsed product price",
                "verbose_name_plural": "Parsed product prices",
            },
        ),
    ]
