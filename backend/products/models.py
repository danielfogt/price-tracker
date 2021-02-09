from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ShopData(models.Model):
    name = models.CharField(verbose_name=_("Shop name"), unique=True, max_length=255)
    domain = models.CharField(
        verbose_name=_("Valid domain name"), unique=True, max_length=120
    )
    logo = models.ImageField(
        upload_to="assets/images", default="no-image-available.jpg", blank=True
    )

    class Meta:
        verbose_name = "Shop data"
        verbose_name_plural = "Shops data"

    def __str__(self):
        return self.domain


class Product(models.Model):
    product_name = models.CharField(
        verbose_name=_("Product name"), unique=True, max_length=255
    )
    last_parsing_data = models.DateTimeField(
        verbose_name=_("Last parsing price product date"), null=True, blank=True
    )
    users = models.ManyToManyField(
        User,
        verbose_name=_("Assigned users"),
        blank=True,
        related_name="favourite_products",
    )
    url_to_scrape_product = models.URLField(
        verbose_name=_("Url to scrape product"), unique=True
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name


class ProductShop(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        related_name="product_shop",
        on_delete=models.SET_NULL,
        null=True,
    )
    shop_product_name = models.CharField(
        verbose_name=_("Shop product name"), unique=True, max_length=255
    )
    ean = models.CharField(
        verbose_name=_("EAN Code"), max_length=17, blank=True, null=True
    )
    price = models.FloatField(
        verbose_name=_("Gross Price"),
        blank=False,
        null=False,
        validators=[MinValueValidator(0, _("Price cannot be less than 0!"))],
    )
    delivery_price = models.FloatField(
        verbose_name=_("Delivery Price"),
        blank=False,
        null=False,
        validators=[MinValueValidator(0, _("Price cannot be less than 0!"))],
    )
    url_to_shop = models.URLField(verbose_name=_("Url to shop"), unique=True)
    shop = models.ForeignKey(
        ShopData,
        verbose_name=_("Shop"),
        related_name="product",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "Product Shop"
        verbose_name_plural = "Products Shop"

    def __str__(self):
        return self.url_to_shop

    @property
    def total_price(self):
        return self.price + self.delivery_price
