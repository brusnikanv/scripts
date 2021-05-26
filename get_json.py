import requests, json, time
from connect import connect_device

def check_status():
    while True:
        try:
            content = requests.get("https://10.16.8.87/monitoring/", verify=False, timeout=20)
        except:
            telegram_bot_sendtext('server not resolve')

        json_data = dict(json.loads(content.content))
        services_status = json_data['servers']
        devices_list = json_data['devices']


        for service_status in services_status.items():
            #print(service_status[0])
            #print(service_status[1]['status'])
            service_name = service_status[0]
            srv_status = service_status[1]['status']

            if srv_status != 1:
                telegram_bot_sendtext('Service Core Down - {0}'.format(service_name))

        for device in devices_list.items():
            dvc_name = device[0]
            dvc_status = device[1]['status']
            print(device[1]['status'])
            dvc_services = json.dumps(device[1]['subservices']).replace("_", "")
            print(dvc_services)

            #тут изменить обратно на правильный статус 2
            if dvc_status == 1:
                #save log to file
                connect_device()
                print(telegram_bot_sendtext('Device services has Problem - {0} {1}'.format(dvc_name, dvc_services)))

            elif dvc_status == 0:
                telegram_bot_sendtext('Device Down - {0}'.format(dvc_name))

            else:
                pass
            time.sleep(10)


# Telegram Bot
def telegram_bot_sendtext(bot_message):
    bot_token = '1400084494:AAGJX-WtbA6eJy0PAwe7u2Jtsnzp7bpSuXU'
    bot_chatID = '-381749129'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


if __name__ == "__main__":
    check_status()