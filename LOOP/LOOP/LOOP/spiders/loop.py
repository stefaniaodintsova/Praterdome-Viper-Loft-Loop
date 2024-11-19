import json
import requests
from datetime import datetime

with open('loop.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list) and len(data) > 0:
    first_item = data[0]

    events = first_item.get('events', [])

    token = '7873262995:AAFim-93kmH76N45TYHh-RCt9JmnFNMipaU'
    method = "sendMessage"
    chat_id = -1002377541779
    #chat_id = -1002387048313 TEST

    failed_events = []

    today_date = datetime.today().strftime('%Y-%m-%d')

    for event in events:
        title = event.get('title', 'No Title')  # Ošetríme chýbajúce kľúče
        event_date = event.get('date', 'No Date')
        image_url = event.get('image', 'No Image')

        if event_date == today_date:
            message = (f"📌 Event: {title}\n"
                       f"📅 Date: {event_date}\n"
                       f"📍 Location: LOOP\n"
                       f"🔗 Link: https://loop.co.at/events/\n"
                       f"🖼️ Image: {image_url}")

            response = requests.post(f'https://api.telegram.org/bot7545702514:AAG4FIXbWtOsgcoJuZAzPYnLjg0LFDP-asc/sendMessage', data={
                'chat_id': chat_id,
                'text': message
            })

            if response.status_code != 200:
                failed_events.append(title)

    if failed_events:
        print("Failed to send messages for the following events:")
        for failed in failed_events:
            print(failed)
    else:
        print("All messages were successfully sent!")

else:
    print("The JSON structure is not as expected or the list is empty.")
