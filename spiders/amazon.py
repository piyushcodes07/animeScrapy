import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/boAt-Immortal-IM1000D-Headphones-Breathing/dp/B095XHFFDY/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=e2ykk"]

    def parse(self, response):
        pass
