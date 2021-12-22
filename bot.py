import aiogram
from aiogram import Bot, Dispatcher, executor, types
from dispatcher import dp
import handlers
from db import BotDB
import aioschedule
import asyncio
from dispatcher import bot
ver = 1.3
BotDB = BotDB('mood_bot.db')

async def choose_your_dinner():

    await bot.send_message('454025767', "Хей🖖 \n Это тест рассылки")
async def scheduler():
    aioschedule.every().day.at("02:00").do(choose_your_dinner)
    aioschedule.every().day.at("02:01").do(choose_your_dinner)
    aioschedule.every().day.at("02:02").do(choose_your_dinner)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
async def on_startup(_):
    asyncio.create_task(scheduler())



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
print('Version bot - ', ver)
