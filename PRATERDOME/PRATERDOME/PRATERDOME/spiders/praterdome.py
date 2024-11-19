import json
import requests


def send_data_to_telegram():
    json_file = 'praterdomestore.json'
    with open(json_file, 'r') as file:
        data = json.load(file)

    #bot_token = '7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE'
    #chat_id = '-1002353949803'

    bot_token = '7672829764:AAEuNRPH_geZc1b4HG2tckQdncczKl2S9RE'
    chat_id = -1002471167965
    #chat_id = -1002387048313 TEST

    for event in data:
        event_title = event['event_title']
        event_link = event['event_link']
        event_date = event['date']
        event_location = event['location']

        w = f"Title: {event_title}\nDate: {event_date}\nLink: {event_link}\nLocation: {event_location}\n"

        requests.post(
            url=f'https://api.telegram.org/bot7672829764:AAEuNRPH_geZc1b4HG2tckQdncczKl2S9RE/sendMessage',
            data={'chat_id': chat_id, 'text': w}
        )


send_data_to_telegram()




# import json
# import requests
#
# def send_data_to_telegram():
#     json_file = '../Praterdome/praterdomestore.json'
#     with open(json_file, 'r') as file:
#         data = json.load(file)
#
#     bot_token = '7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE'
#     # chat_id = '-1002353949803'
#
#     index = 0
#     while index < len(data):
#         event = data[index]
#         event_title = event['event_title']
#         event_link = event['event_link']
#         event_date = event['date']
#         event_location = event['location']
#
#         print(data)
#         index += 1
#
#         n = 0
#         x = len(data)
#         print(x)
#
#         while n < x:
#             w = f"Title: {event_title}\nDate: {event_date}\nLink: {event_link}\nLocation: {event_location}\n"
#
#             print(w)
#             requests.post(
#                 url = f'https://api.telegram.org/bot7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE/sendMessage?chat_id=-1002353949803&text=%s' % w)
#
#             #'https://api.telegram.org/bot7582469146:AAE7beXO058-YbHuiArJp3YK3LjfT0sCZvE-1002353949803text=%s' % w)
#             n += 1
#
#         # Make the request
#         # response = requests.post(url, json=payload)
#         # Format the message
#         # message = f"Title: {event_title}\nDate: {event_date}\nLocation: {event_location}"
#
# send_data_to_telegram()