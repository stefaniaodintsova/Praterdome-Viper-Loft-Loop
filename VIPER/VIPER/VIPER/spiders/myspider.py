import scrapy

class ViperSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        'https://www.viper-room.at/veranstaltungen',
    ]

    custom_settings = {
        'FEEDS': {
            'viperroom_events.json': {
                'format': 'json',
                'overwrite': True,
                'indent': 4,
            },
        },
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 1,
    }

    def parse(self, response):
        self.log(f"Processing the website: {response.url}")

        events = response.xpath('//ul[@class="events_list"]/li')

        for event in events:
            title = event.xpath('.//h2[@class="event_title"]/a/text()').get().strip()

            link = event.xpath('.//h2[@class="event_title"]/a/@href').get()
            event_url = response.urljoin(link)

            date = event.xpath('.//div[@class="event_date_monthyear"]/text()').get().strip()

            location = 'Viper Room Vienna, Landstrasser Hauptstr. 38, 1030 Wien, Österreich'

            yield {
                'title': title,
                'link': event_url,
                'date': date,
                'location': location,
            }
