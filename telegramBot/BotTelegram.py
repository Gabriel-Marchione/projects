import telepot
from wikiScraping import wikiFun

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'].find('wikipedia') != -1 and msg['text'].find('https') != -1:
            link = msg['text']
            page = wikiFun(link)
            bot.sendMessage(chat_id,page)
            bot.sendMessage(chat_id,'Paste Wikipedia s link.')
            
TOKEN = '1058870398:AAHluYmy-z6e8STd7rJIS2HubLLnoGgn54U'

bot = telepot.Bot(TOKEN)
bot.sendMessage(394940086,'Paste Wikipedia s link.')
bot.message_loop(on_chat_message)
print('Listening ...')


import time
while 1:
    time.sleep(10)
