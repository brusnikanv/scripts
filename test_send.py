import requests

def telegram_bot_sendtext(bot_message):

   bot_token = '1235046508:AAHKVU8haT0wxTsnu6dPtJGfNYLQPvQs2yg'
   bot_chatID = '294251325'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("ALaaarma")