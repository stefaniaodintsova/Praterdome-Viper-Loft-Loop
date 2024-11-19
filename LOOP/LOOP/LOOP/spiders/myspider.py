import scrapy
import json
from datetime import date
from dateutil import parser

# Get today's date
today = date.today().strftime('%Y-%m-%d')

class MySpider(scrapy.Spider):
    name = 'mySpider'
    start_urls = [
        'https://loop.co.at/events/'
    ]
    print(start_urls)
    custom_settings = {
        'FEEDS': {
            'loop.json': {
                'format': 'json',
                'overwrite': True,  # If the file already exists, it will overwrite it
                'indent': 4,  # Better readable
            },
        },
    }

    def parse(self, response):
        date_info = response.xpath('//div[contains(@class, "avia_textblock")]/h2/strong/text()').getall()
        event_titles = response.xpath('//div[contains(@class, "avia_textblock")]/h3/span[@lang="en-AT"]/text() | //div[contains(@class, "avia_textblock")]/h3[1]/text() | //div[contains(@class, "avia_textblock")]/h3/span/text()').getall()
        event_images = response.xpath('//div[contains(@class, "avia-image-overlay-wrap")]/a/img/@src').getall()

        self.log(f"Extracted date info: {date_info}")
        self.log(f"Extracted event titles: {event_titles}")
        self.log(f"Extracted event images: {event_images}")

        if len(date_info) != len(event_titles) or len(date_info) != len(event_images):
            self.log("Warning: The number of dates, event titles, and images do not match!")

        events = []
        for title, date_str, image in zip(event_titles, date_info, event_images):
            try:
                event_date = parser.parse(date_str, dayfirst=True, fuzzy=True).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                event_date = "Unknown"

            events.append({
                'title': title.strip() if title else 'No Title',
                'date': event_date,
                'image': image.strip() if image else 'No Image'
            })

        yield {
            'events': events
        }