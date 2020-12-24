import requests, json


def check_status():
    content = requests.get("https://10.16.8.90/monitoring/", verify=False)
    json_data = dict(json.loads(content.content))
    # print(json_data['servers']['core']['status'])
    services_status = json_data['servers']
    devices_status = json_data['devices']

    # status_list = [core_status, devices_status]

    for service_status in services_status.items():
        print(service_status[0])
        print(service_status[1]['status'])
        service_name = service_status[0]
        srv_status = service_status[1]['status']

        if srv_status == 1:
            print('server_ok')
        else:
            telegram_bot_sendtext('Service Down - {0}'.format(service_name))


# Telegram Bot
def telegram_bot_sendtext(bot_message):
    bot_token = '1235046508:AAHKVU8haT0wxTsnu6dPtJGfNYLQPvQs2yg'
    bot_chatID = '-381749129'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


if __name__ == "__main__":
    check_status()
