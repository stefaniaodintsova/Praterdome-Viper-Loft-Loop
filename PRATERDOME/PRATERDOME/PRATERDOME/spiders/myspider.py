import scrapy

class PraterDomeSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        'https://praterdome.at/en/events',
    ]

    custom_settings = {
        'FEEDS': {
            'praterdomestore.json': {  # Output file name
                'format': 'json',  # File format
                'overwrite': True,  # Overwrite file on each run
                'indent': 4,  # Pretty JSON formatting
            },
        },
    }

    def parse(self, response, event_title=None):
        self.log(f"Processing page: {response.url}")

        # Locate all events on the page
        events = response.xpath('//div[contains(@class, "event-snippet")]')

        for event in events:
            # Extract event details
            date = f"{event.xpath('.//span[@class="event-date-cal-weekday"]/text()').get()}, {event.xpath('.//span[@class="event-date-cal-day"]/text()').get()} {event.xpath('.//span[@class="event-date-cal-month"]/text()').get()}"
            location = 'Prater Dome, Riesenradplatz 7, 1020 Vienna'  # Default location

            # Extract event link from the image
            image_link = event.xpath('.//div[@class="thumbnail"]/a/@href').get()
            event_link = response.urljoin(image_link) if image_link else 'No link available'

            # Extract event image source
            image_src = event.xpath('.//div[@class="thumbnail"]/a/img/@src').get()
            image_src = response.urljoin(image_src) if image_src else 'No image available'

            # Extract event title
            title = event.xpath('.//h4[@class="title mt--0"]/a/text()').get().strip() if event.xpath(
                './/h4[@class="title mt--0"]/a/text()').get() else 'NO TITLE'

            # Store the data in a dictionary
            event_data = {
                'event_link': event_link,
                'event_title': title,
                'date': date,
                'location': location,
                'image': image_src,  # Add image URL to the event data
            }

            # Yield the event data
            yield event_data



# import scrapy
#
# class EventsSpider(scrapy.Spider):
#     name = "myspider"
#     start_urls = [
#         'https://praterdome.at/en/',
#     ]
#
#     def parse(self, response):
#         # Extract event data from the page
#         events = response.css('.event-list-item')  # This selector needs to match the event list structure
#         for event in events:
#             title = event.css('h3.event-title::text').get()
#             link = event.css('a::attr(href)').get()
#             location = event.css('.event-location::text').get()
#
#             # Clean up location if needed (strip spaces, remove extra text)
#             location = location.strip() if location else "No location provided"
#
#             yield {
#                 'title': title,
#                 'link': response.urljoin(link),  # Ensure the link is absolute
#                 'location': location
#             }
#
#         # If the site has pagination, follow next page links (if any)
#         next_page = response.css('a.next::attr(href)').get()
#         if next_page:
#             yield response.follow(next_page, self.parse)