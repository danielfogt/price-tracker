import scrapy

from django.utils import timezone

from products.scrapers.ceneo.items import CeneoProduct

CHOSEN_CATEGORY_TO_PARSE_XPATH = (
    "//dl[@class='category-links']//a[@href='/Komputery']//ancestor::dl"
)


class NewProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.ceneo.pl/SiteMap.aspx"]

    def parse(self, response, **kwargs):
        product_page_links = response.xpath(
            f"{CHOSEN_CATEGORY_TO_PARSE_XPATH}//li[not(@id) and not(@class)]/a"
        ).css("::attr(href)")
        yield from response.follow_all(product_page_links, self.parse_products)

    def parse_products(self, response):
        cat_prod_type_to_find = '//div[@class="cat-prod-row__body"]'
        product_desc_type_to_find = './/strong[@class="cat-prod-row__name"]/a'
        products = response.xpath(cat_prod_type_to_find)
        if not products:
            cat_prod_type_to_find = '//div[@class="cat-prod-box__body"]'
            product_desc_type_to_find = './/strong[@class="cat-prod-box__name"]/a'
            products = response.xpath(cat_prod_type_to_find)

        for product in products:
            product_desc = product.xpath(product_desc_type_to_find)
            if not product_desc:
                continue
            product_url = product_desc.css("::attr(href)").get()
            if product_url.startswith("/Click/Offer"):
                continue
            product_name = product_desc.css("::text").get().strip()

            price = "".join(
                product.xpath('.//span[@class="price"]//text()').getall()
            ).replace(",", ".")

            item = CeneoProduct()
            item["product_name"] = product_name
            item["url_to_scrape_product"] = f"https://www.ceneo.pl{product_url}"
            item["last_parsed_price"] = price
            yield item

        next_page = response.xpath('//a[@alt="Następna"]').css("::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_products)
