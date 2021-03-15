import scrapy
from scrapy.crawler import CrawlerProcess

class BitcoinSpider(scrapy.Spider):
    name = 'bitcoin'
    start_urls = ['https://www.coindesk.com/price/bitcoin']

    def parse(self, response):
        yield {
            "price": response.css(".price-large::text").getall()[0],
            "percentage_change_value": response.css(".percent-value-text::text").getall()[0],
            "market_cap": response.css(".price-medium::text").getall()[0],
            "24-low": response.css(".price-medium::text").getall()[1],
            "24-high": response.css(".price-medium::text").getall()[3],
            "transaction count in last 24 hour": response.css(".price-medium::text").getall()[-3],
            "Avg transaction fee": response.css(".price-medium::text").getall()[-2],
            "VALUE TRANSACTED in last 24 hour": response.css(".price-medium::text").getall()[-1],
            "net change": response.css(".price-change-medium::text").getall()[0],
            "All time high": response.css(".price-small::text").getall()[0],
        }

# process = CrawlerProcess()
# process.crawl(BitcoinSpider)
# process.start()
