import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://www.ceneo.pl/SiteMap.aspx"]

    def parse(self, response, **kwargs):
        product_page_links = response.xpath("//li[not(@id) and not(@class)]/a").css(
            "::attr(href)"
        )
        yield from response.follow_all(product_page_links[:10], self.parse_products)

    def parse_products(self, response):
        parsed_products = {"urls": []}
        products = response.xpath('//strong[@class="cat-prod-row__name"]/a')
        if products:
            for product in products:
                product_url = product.css("::attr(href)").get()
                product_name = product.css("::text").get()
                parsed_products["urls"].append(product_url)
        else:
            products = response.xpath('//strong[@class="cat-prod-box__name"]/a')
            for product in products:
                product_url = product.css("::attr(href)").get()
                product_name = product.css("::text").get()
                parsed_products["urls"].append(product_url)
        yield parsed_products

        next_page = response.xpath('//a[@alt="Następna"]').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_products)
