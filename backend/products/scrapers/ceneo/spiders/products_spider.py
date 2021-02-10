import scrapy

from django.utils import timezone

from products.scrapers.ceneo.items import CeneoItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.ceneo.pl/SiteMap.aspx"]

    def parse(self, response, **kwargs):
        product_page_links = response.xpath("//li[not(@id) and not(@class)]/a").css(
            "::attr(href)"
        )
        yield from response.follow_all(product_page_links[:1], self.parse_products)

    def parse_products(self, response):
        cat_prod_type_to_find = '//div[@class="cat-prod-row__body"]'
        product_desc_type_to_find = './strong[@class="cat-prod-row__name"]/a'
        products = response.xpath(cat_prod_type_to_find)
        if not products:
            cat_prod_type_to_find = '//div[@class="cat-prod-box__body"]'
            product_desc_type_to_find = './strong[@class="cat-prod-box__name"]/a'
            products = response.xpath(cat_prod_type_to_find)

        for product in products:
            product_desc = product.xpath(product_desc_type_to_find)
            product_url = product_desc.css("::attr(href)").get()
            product_name = product_desc.css("::text").get().strip()

            price = "".join(
                product.xpath('.//span[@class="price"]//text()').getall()
            ).replace(",", ".")

            item = CeneoItem()
            item["product_name"] = product_name
            item["url_to_scrape_product"] = product_url
            item["last_parsing_data"] = timezone.now()
            item["last_parsed_price"] = price
            yield item

        next_page = response.xpath('//a[@alt="Następna"]').css("::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_products)
