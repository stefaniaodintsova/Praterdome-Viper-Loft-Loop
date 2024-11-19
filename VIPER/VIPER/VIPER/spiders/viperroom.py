import requests
import json

TOKEN = '7958779435:AAHkYL-e0anpkU-SktSENyAj1bCjRnB5yB0'
CHANNEL_ID = -1002260178090
#CHANNEL_ID = -1002387048313 TEST

def send_telegram_message(message):
    print(f"Sending message to Telegram:\n{message}")
    response = requests.post(
        f'https://api.telegram.org/bot7958779435:AAHkYL-e0anpkU-SktSENyAj1bCjRnB5yB0/sendMessage',
        data={'chat_id': CHANNEL_ID, 'text': message, 'parse_mode': 'Markdown'}
    )
    print(f"Telegram response: {response.status_code} - {response.json()}")
    return response.json()

def load_events_from_file():
    try:
        with open('viperroom_events.json', 'r', encoding='utf-8') as file:
            events = json.load(file)
            print(f"Loaded {len(events)} events from file.")
            return events
    except FileNotFoundError:
        print("The file 'viperroom_events.json' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error parsing the JSON file.")
        return []

events = load_events_from_file()

for event in events:
    title = event.get('title', 'Unknown title')
    start_date = event.get('date', 'Unknown date')
    location = event.get('location', 'Viper Room')
    link = event.get('link', 'No link available')

    message = (
        f"📅 *Event*: {title}\n"
        f"🗓 *Date*: {start_date}\n"
        f"📍 *Location*: Viper Room\n"
        f"🔗 {link}"
    )

    response = send_telegram_message(message)