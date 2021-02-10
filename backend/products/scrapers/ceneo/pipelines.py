# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from products.models import Product
from products.scrapers.ceneo.items import CeneoProduct


class CeneoPipeline:
    def process_item(self, item, spider):
        if isinstance(item, CeneoProduct):
            Product.objects.update_or_create(
                url_to_scrape_product=item["url_to_scrape_product"], defaults={**item}
            )
            return item
