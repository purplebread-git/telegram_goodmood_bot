import aiogram
from aiogram import Bot, Dispatcher, executor, types
from dispatcher import dp
import handlers
from db import BotDB

ver = 1.0

BotDB = BotDB('mood_bot.db')
print("Hello")
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)