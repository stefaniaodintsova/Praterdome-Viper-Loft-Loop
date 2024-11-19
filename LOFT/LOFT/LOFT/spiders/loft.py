import json
import requests
from datetime import datetime

with open('loft.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if isinstance(data, list) and len(data) > 0:
    first_item = data[0]

    events = first_item.get('events', [])

    token = '7545702514:AAG4FIXbWtOsgcoJuZAzPYnLjg0LFDP-asc'
    method = "sendMessage"
    chat_id = -1002273754149
    #chat_id = -1002387048313 TEST

    failed_events = []

    today_date = datetime.today().strftime('%Y-%m-%d')

    for event in events:
        title = event.get('title', 'No Title')
        event_date = event.get('date', 'No Date').strip()

        location = event.get('location', 'No Location')
        open_time = event.get('open', 'No Open Time')
        link = event.get('link', 'No Link')

        if event_date == today_date:
            message = f"🎉 Event: {title}\n📅 Date: {event_date}\n📍 Location: {location}\n⏰ Time: {open_time}\n🔗 Link: {link}"

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
        print("All messages for today's events were successfully sent!")

else:
    print("The JSON structure is not as expected or the list is empty.")