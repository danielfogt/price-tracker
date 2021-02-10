from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("product_name", "url_to_scrape_product")


admin.site.register(Product, ProductAdmin)
