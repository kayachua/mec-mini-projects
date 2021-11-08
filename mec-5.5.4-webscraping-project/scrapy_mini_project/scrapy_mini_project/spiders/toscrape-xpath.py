import scrapy


class QuotesSpiderXpath(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'text': quote.xpath(".//span[@class='text']//text()").get(),
                'author': quote.xpath(".//span//small//text()").get(),
                'tags': quote.xpath(".//div[@class='tags']//a[@class='tag']//text()").getall(),
            }

        yield from response.follow_all(css='ul.pager a', callback=self.parse)
