import telebot
import time
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

def send_clip(clip_path, nick):
    clip = open(clip_path, 'rb')
    bot.send_video(CHANNEL_ID, clip, caption=nick, timeout=100)
    clip.close()
    os.remove(clip_path)
    print("\nSENT AND REMOVED {}".format(clip_path))
    time.sleep(1800)


