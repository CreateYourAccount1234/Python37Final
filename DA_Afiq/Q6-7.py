import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["http://172.17.50.43/snow"]
    def parse(self, response):
        css_sel = "img"
        for x in response.css(css_sel):
            xpath = "@src"
            css_sel = "::attr(src)"
            yield {
                "image Link":x.xpath(xpath).extract_first(),
            }
            nextcss_sel = ".next a::attr(href)"
            next_page = response.css(nextcss_sel).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page),callback=self.parse())

