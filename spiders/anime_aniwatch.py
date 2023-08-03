import scrapy


class AnimeAniwatchSpider(scrapy.Spider):
    name = "anime_aniwatch"
    allowed_domains = ["aniwatch.to"]
    start_urls = ["https://aniwatch.to/home"]

    def parse(self, response):
        popular_anime_latest=response.css("#trending-home div.swiper-container div.swiper-wrapper div.swiper-slide")

        for anime in popular_anime_latest:
            yield{
                "number":anime.css("div.number span::text").get(),
                "poster-image":anime.css("img::attr(data-src)").get(),
                "title":anime.css("img::attr(title)").get()
            }