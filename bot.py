import telebot
import time
import os

TOKEN = "1250883576:AAFe-Wp9Uk4lVRX3syccH6ALbs91bsBSkXA"
bot = telebot.TeleBot(TOKEN)

def send_clip(clip_path, nick):
    clip = open(clip_path, 'rb')
    bot.send_message(285999952, 'aaaaaaa')
    bot.send_video(285999952, clip, caption=nick, timeout=100)
    clip.close()
    os.remove(clip_path)
    print("\nSENT AND REMOVED {}".format(clip_path))
    time.sleep(1800)



# channel -1001454098114
# me 285999952
