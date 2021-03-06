from aiogram import types
from dispatcher import dp
import re
from bot import BotDB, ver
from draw_table import draw_function
from PIL import Image, ImageDraw
global markup, markup_mood
count = 0

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица меню -.-.-.-.-.-.-.-.-.-.-.-.-

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("➕ Добавить запись")
item2 = types.KeyboardButton("📊  Статистика")
item3 = types.KeyboardButton("⚙️Настройки")
markup.add(item1, item2, item3)

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица выбора настроения -.-.-.-.-.-.-.-.-.-.-.-.-

markup_mood = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton(" 😀 ", callback_data='nice')
item2 = types.KeyboardButton(" 🙂 ", callback_data='good')
item3 = types.KeyboardButton(" 😕 ", callback_data='-')
item4 = types.KeyboardButton(" 😔 ", callback_data='bad')
item5 = types.KeyboardButton(" 😭 ", callback_data='verybad')
item6 = types.KeyboardButton("🔙 Назад", callback_data='back')
markup_mood.add(item1, item2, item3, item4, item5, item6)

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица статистики -.-.-.-.-.-.-.-.-.-.-.-.-


markup_statistic = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("📈 График за неделю")
item2 = types.KeyboardButton("📈 График за месяц")
item3 = types.KeyboardButton("📈 График за год")
item4 = types.KeyboardButton("📁 Экспорт XML")
item5 = types.KeyboardButton("🔙 Назад")
markup_statistic.add(item1, item2, item3, item4, item5)


# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица настроек -.-.-.-.-.-.-.-.-.-.-.-.-


markup_settings = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("👤 Профиль")
item2 = types.KeyboardButton("🔔 Напоминания")
item3 = types.KeyboardButton("🤖 О боте")
item4 = types.KeyboardButton("🔙 Назад")
markup_settings.add(item1, item2, item3, item4)


# -.-.-.-.-.-.-.-.-.-.-.-.- Старт -.-.-.-.-.-.-.-.-.-.-.-.-

@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=markup)


# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

@dp.message_handler()
async def echo_message(message: types.Message):
    global count
    print('count_1 = ', count)
    msg = message['text']
    print(msg)
    if msg == "➕ Добавить запись":
        await message.bot.send_message(message.from_user.id, "Выберите Ваше <b>настроение</b> <u>сейчас</u>!",
                                       reply_markup=markup_mood)
        count = 1
    elif count == 1:
        print('1')
        if msg == " 😀 ":
            mood = 5
            BotDB.add_record(message.from_user.id, mood)
            await message.bot.send_message(message.from_user.id,
                                           "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                           reply_markup=markup)
            count = 0
        elif msg == " 🙂 ":
            mood = 4
            BotDB.add_record(message.from_user.id, mood)
            await message.bot.send_message(message.from_user.id,
                                           "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                           reply_markup=markup)
            count = 0
        elif msg == " 😕 ":
            mood = 3
            BotDB.add_record(message.from_user.id, mood)
            await message.bot.send_message(message.from_user.id,
                                           "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                           reply_markup=markup)
            count = 0
        elif msg == " 😔 ":
            mood = 2
            BotDB.add_record(message.from_user.id, mood)
            await message.bot.send_message(message.from_user.id,
                                           "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                           reply_markup=markup)
            count = 0
        elif msg == " 😭 ":
            mood = 1
            BotDB.add_record(message.from_user.id, mood)
            await message.bot.send_message(message.from_user.id,
                                           "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                           reply_markup=markup)
            count = 0
        elif msg == "🔙 Назад":
            await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню", reply_markup=markup)
            count = 0

    elif msg == "📊  Статистика":
        await message.bot.send_message(message.from_user.id, "Статистика", reply_markup=markup_statistic)
        count = 2
    elif count == 2:
        if msg == "📈 График за неделю":
            records_week = BotDB.get_records(message.from_user.id, 'week')
            print('records_week - ', records_week)
            print('len - ', len(records_week))
            if len(records_week):
                draw_function('week', records_week)

                await message.bot.send_message(message.from_user.id, 'Ваша статистика настроений за неделю', reply_markup=markup)
                await message.bot.send_photo(message.from_user.id, open('pic.png', 'rb'))
                count = 0
            else:
                await message.bot.send_message(message.from_user.id, 'Записей не обнаружено', reply_markup=markup)
                count = 0
        if msg == "📈 График за месяц":
            records_month = BotDB.get_records(message.from_user.id, 'month')
            if len(records_month):
                record_all = []
                for i in range(0, len(records_month)):
                    record = []
                    rec = records_month[i]
                    record.append(str(rec[3]))
                    record.append(str(rec[2]))
                    record_all.append(' - '.join(record))
                r = '\n'.join(record_all)
                await message.bot.send_message(message.from_user.id, 'Ваша статистика настроений за месяц  \n\n' + r, reply_markup=markup)
                count = 0
            else:
                await message.bot.send_message(message.from_user.id, 'Записей не обнаружено', reply_markup=markup)
                count = 0
        if msg == "📈 График за год":
            records_year = BotDB.get_records(message.from_user.id, 'year')
            if len(records_year):
                record_all = []
                for i in range(0, len(records_year)):
                    record = []
                    rec = records_year[i]
                    record.append(str(rec[3]))
                    record.append(str(rec[2]))
                    record_all.append(' - '.join(record))
                r = '\n'.join(record_all)
                await message.bot.send_message(message.from_user.id, 'Ваша статистика настроений за год  \n\n' + r, reply_markup=markup)
                count = 0
            else:
                await message.bot.send_message(message.from_user.id, 'Записей не обнаружено', reply_markup=markup)
                count = 0
        if msg == "📁 Экспорт XML":
            await message.bot.send_message(message.from_user.id, "Доступно только в <b>Premium</b>", reply_markup=markup_statistic)
        if msg == "🔙 Назад":
            await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню", reply_markup=markup)
            count = 0

    elif msg == "⚙️Настройки":
        await message.bot.send_message(message.from_user.id, "Настройки", reply_markup=markup_settings)
        count = 3
    elif count == 3:
        if msg == "👤 Профиль":
            await message.bot.send_message(message.from_user.id, "Профиль", reply_markup=markup_settings)
        if msg == "🔔 Напоминания":
            await message.bot.send_message(message.from_user.id, "Напоминания", reply_markup=markup_settings)
        if msg == "🤖 О боте":
            stroke = "Версия бота - "+str(ver)
            stroke1 = "<b>GoodMood</b> - Это отличный бот для людей, которые предпочитают визуально выбирать, что они чувствуют, чем словами описывать своё состояние.\n\n GoodMood включает в себя инструмент «Статистика», который позволяет записывать ваше настроение таким образом, чтобы вы могли выявить закономерности в своих чувствах и поведении. Вы всегда можете проанализировать свои предыдущие записи, чтобы в конечном итоге научиться анализировать своё настроение и  справляться с депрессией.\n\n Версия бота - " + str(ver) + "\n\nВопросы и предложения - @purple_bread"
            await message.bot.send_message(message.from_user.id, stroke1, reply_markup=markup)
            count = 0
        if msg == "🔙 Назад":
            await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню", reply_markup=markup)
            count = 0
    elif msg == "🖋 Редактировать последнюю запись":
        await message.bot.send_message(message.from_user.id, "Редактировать последнюю запись", reply_markup=markup)
        count = 4
    elif msg == "/secret":
        await message.bot.send_message(message.from_user.id, "Люблю тебя, Поля!", reply_markup=markup)
        await message.answer_sticker(r'CAACAgIAAxkBAAEDZmVhqMklwbAWpOwq6Ia9PVS6nJbM7wACFwMAAladvQrnhi7ExlTFGyIE')
        count = 0
    else:
        try:
            await message.bot.send_message(message.from_user.id, "Ошибка", reply_markup=markup)
        except:
            print('Там у кого-то ошибка')
    print('count_2 = ', count)
    print('-----------------------------')


