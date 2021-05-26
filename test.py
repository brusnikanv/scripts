import telegram

def send_msg(text):
    token = '1400084494:AAGJX-WtbA6eJy0PAwe7u2Jtsnzp7bpSuXU'
    chat_id = '-381749129'
    bot = telegram.Bot(token=token)
    for i in text:
        bot.sendMessage(chat_id=chat_id, text=i)

new_list = []
with open("filename.txt", 'r', encoding="utf-8") as file:
     new_list = file.read()
for i in new_list:
     send_msg(i)