from aiogram import types
from dispatcher import dp
from bot import BotDB, ver
from draw_table import draw_function
from config import admin_id, kanal_id, polya_id
import os
from markups import markup, markup_start, markup_mood, markup_podpisk, markup_statistic, markup_admin, markup_settings, markup_back
global markup, markup_mood
count = 0
global user_status


# -.-.-.-.-.-.-.-.-.-.-.-.- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
@dp.callback_query_handler(text='ready')
async def ready_start(call: types.CallbackQuery):
    msg_id = call['message']
    await call.bot.delete_message(call.from_user.id, int(msg_id['message_id']))

# -.-.-.-.-.-.-.-.-.-.-.-.- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

@dp.callback_query_handler(text='podpisk')
async def check_podpisk(call: types.CallbackQuery):
    user_status = await call.bot.get_chat_member(chat_id=kanal_id, user_id=call.from_user.id)
    msg_id = call['message']
    msg_start = '''<b>Как пользоваться ботом:</b>\n\n
➕ <b>Добавить запись</b> - Нажмите, чтобы добавить запись о Вашем настроении на данный момент \n\n
📊 <b>Статистика</b> - Нажмите, чтобы открыть панель статистики \n
- 📈 <b>Вывод графика</b> за определенный период (неделя/месяц/год) \n
- 📁 <b>Экспорт XML</b> - Данная функция еще находится в разработке \n\n
⚙️<b>Настройки</b> - Нажмите, чтобы открыть панель настроек бота \n
- 👤 <b>Профиль</b> - В данном разделе Вы можете посмотреть подробную информацию о своём профиле в боте \n
- 🔔 <b>Напоминания</b> - В этом разделе Вы можете установить количество и время для напоминаний о записи настроения \n
- 🤖 <b>О боте</b> - А в это разделе Вы можете посмтореть информацию о боте'''

    if user_status['status'] != 'left':
        await call.bot.delete_message(call.from_user.id, int(msg_id['message_id']))
        await call.bot.send_message(call.from_user.id, "Вы успешно подписались на канал, спасибо!", reply_markup=markup)
        await call.bot.send_message(call.from_user.id, msg_start, reply_markup=markup_start)
    else:
        await call.bot.send_message(call.from_user.id, "Извините, но Вы не подписались на канал",
                                    reply_markup=markup_podpisk)

# -.-.-.-.-.-.-.-.-.-.-.-.- Старт -.-.-.-.-.-.-.-.-.-.-.-.-

@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)
    await message.bot.delete_message(message.from_user.id, int(message['message_id']))
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!")
    msg_kan = 'Для использования бота, пожалуйста, подпишитесь на канал' + '\n\n' + 'https://t.me/goodmood_kanal'
    await message.bot.send_message(message.from_user.id, msg_kan, reply_markup=markup_podpisk)


# -.-.-.-.-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

@dp.message_handler()
async def echo_message(message: types.Message):
    global count
    print('count_1 = ', count)
    msg = message['text']
    print((message['from'])['first_name'],' - ',msg)
    print(message.from_user.id)

    user_status = await message.bot.get_chat_member(chat_id=kanal_id, user_id=message.from_user.id)
    if user_status['status'] != 'left' or int(message.from_user.id) == polya_id:

#---------------------------------------------------------

        if msg == "➕ Добавить запись":
            await message.bot.send_message(message.from_user.id, "Выберите Ваше <b>настроение</b> <u>сейчас</u>!",
                                           reply_markup=markup_mood)
            await message.bot.delete_message(message.from_user.id, int(message['message_id']))
            count = 1
        elif count == 1:
            if msg == " 😀 ":
                mood = 5
                BotDB.add_record(message.from_user.id, mood)
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id,
                                               "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                               reply_markup=markup)
                count = 0
            elif msg == " 🙂 ":
                mood = 4
                BotDB.add_record(message.from_user.id, mood)
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id,
                                               "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                               reply_markup=markup)
                count = 0
            elif msg == " 😕 ":
                mood = 3
                BotDB.add_record(message.from_user.id, mood)
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id,
                                               "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                               reply_markup=markup)
                count = 0
            elif msg == " 😔 ":
                mood = 2
                BotDB.add_record(message.from_user.id, mood)
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id,
                                               "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                               reply_markup=markup)
                count = 0
            elif msg == " 😭 ":
                mood = 1
                BotDB.add_record(message.from_user.id, mood)
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id,
                                               "✅ Запись о Вашем <b>настроении</b> успешно внесена!",
                                               reply_markup=markup)
                count = 0
            elif msg == "🔙 Назад":
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню",
                                               reply_markup=markup)
                count = 0
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))

#---------------------------------------------------------

        elif msg == "📊  Статистика":
            await message.bot.delete_message(message.from_user.id, int(message['message_id']))
            await message.bot.send_message(message.from_user.id, "📊  Статистика", reply_markup=markup_statistic)

            count = 2
        elif count == 2:
            if msg == "📈 График за неделю":
                records_week = BotDB.get_records(message.from_user.id, 'week')
                #print('records_week - ', records_week)
                #print('len - ', len(records_week))
                if len(records_week):
                    draw_function('week', records_week, message.from_user.id)
                    await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                    await message.bot.send_message(message.from_user.id, 'Ваша статистика настроений за неделю',
                                                   reply_markup=markup)
                    name_pic = 'pic_' + str(message.from_user.id) + '.png'
                    await message.bot.send_photo(message.from_user.id, open(name_pic, 'rb'))
                    if os.path.isfile(name_pic):
                        os.remove(name_pic)
                    else:
                        await message.bot.send_message(admin_id, "Проблема с удалением png "+str(message.from_user.id), reply_markup=markup)
                    count = 0
                else:
                    await message.bot.delete_message(message.from_user.id, int(message['message_id']))
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
                    await message.bot.send_message(message.from_user.id,
                                                   'Ваша статистика настроений за месяц  \n\n' + r, reply_markup=markup)
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
                    await message.bot.send_message(message.from_user.id, 'Ваша статистика настроений за год  \n\n' + r,
                                                   reply_markup=markup)
                    count = 0
                else:
                    await message.bot.send_message(message.from_user.id, 'Записей не обнаружено', reply_markup=markup)
                    count = 0
            if msg == "📁 Экспорт XML":
                await message.bot.send_message(message.from_user.id, "Временно недоступно",
                                               reply_markup=markup_statistic)
            if msg == "🔙 Назад":
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню",
                                               reply_markup=markup)
                count = 0

#---------------------------------------------------------

        elif msg == "⚙️Настройки":
            await message.bot.delete_message(message.from_user.id, int(message['message_id']))
            await message.bot.send_message(message.from_user.id, "Настройки", reply_markup=markup_settings)
            count = 3
        elif count == 3:
            if msg == "👤 Профиль":
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id, "Профиль", reply_markup=markup_settings)
            if msg == "🔔 Напоминания":
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id, "Напишите сколько раз в день Вы хотите оценивать своё настроение:\n(От 1 до 10)", reply_markup=markup_back)
                count = 3.1
            if msg == "🤖 О боте":
                stroke = "Версия бота - " + str(ver)
                stroke1 = "<b>GoodMood</b> - Это отличный бот для людей, которые предпочитают визуально выбирать, что они чувствуют, чем словами описывать своё состояние.\n\n GoodMood включает в себя инструмент «Статистика», который позволяет записывать ваше настроение таким образом, чтобы вы могли выявить закономерности в своих чувствах и поведении. Вы всегда можете проанализировать свои предыдущие записи, чтобы в конечном итоге научиться анализировать своё настроение и  справляться с депрессией.\n\n Версия бота - " + str(
                    ver) + "\n\nВопросы и предложения - @purple_bread"
                await message.bot.send_message(message.from_user.id, stroke1, reply_markup=markup)
                count = 0
            if msg == "🔙 Назад":
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню",
                                               reply_markup=markup)
                count = 0
        elif count == 3.1:
            if msg == "🔙 Назад":
                await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню",
                                               reply_markup=markup)
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.delete_message(message.from_user.id, int(message['message_id'])-1)
                count = 0
            else:
                try:


                    await message.bot.send_message(message.from_user.id, "Отлично! Теперь ваша ежедневная задача отмечать свое настроение <b>"+str(int(msg))+"</b> в день",
                                                  reply_markup=markup)
                except:
                    await message.bot.send_message(message.from_user.id, "Введите корректное значение - число от 1 до 10", reply_markup=markup_back)

        elif msg == "🖋 Редактировать последнюю запись":
            await message.bot.send_message(message.from_user.id, "Редактировать последнюю запись", reply_markup=markup)
            count = 4
        elif msg == "/secret":
            await message.bot.send_message(message.from_user.id, "Люблю тебя, Поля!", reply_markup=markup)
            await message.answer_sticker(r'CAACAgIAAxkBAAEDZmVhqMklwbAWpOwq6Ia9PVS6nJbM7wACFwMAAladvQrnhi7ExlTFGyIE')
            count = 0
        elif msg == "/admin":
            if int(message.from_user.id) == admin_id:
                await message.bot.send_message(message.from_user.id, "Привет админ!", reply_markup=markup_admin)
                count = 5
            else:
                await message.bot.send_message(message.from_user.id, "Вы не админ, извините!", reply_markup=markup)
                count = 0
        elif msg == "Отправить всем сообщение":
            if count == 5:
                count_text = "Введи сообщение:"
                await message.bot.send_message(message.from_user.id, count_text, reply_markup=markup_admin)
                count = 6
            else:
                await message.bot.send_message(message.from_user.id, "Ошибка", reply_markup=markup)
                count = 0
        elif count == 6:
            c = BotDB.read_sqlite_table()
            msg_z = str(msg)
            if msg_z != '🔙 Назад':
                for i in range(0, len(c)):
                    err = 'Не удалось отправить сообщение -' + str(c[i])
                    try:
                        await message.bot.send_message(int(c[i]), msg_z, reply_markup=markup)
                    except:
                        await message.bot.send_message(admin_id, err, reply_markup=markup)
                await message.bot.send_message(admin_id, 'Отправка успешно завершена', reply_markup=markup)
            else:
                await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню",
                                               reply_markup=markup)
                count = 0
            count = 0
        elif msg == "Кол-во пользователей":
            if count == 5:
                count_users = BotDB.get_count()
                count_text = "Количество пользователей - " + str(count_users[0])
                await message.bot.send_message(message.from_user.id, count_text, reply_markup=markup_admin)
                count = 5
            else:
                await message.bot.send_message(message.from_user.id, "Ошибка", reply_markup=markup)
                count = 0
        elif msg == "🔙 Назад":
            if count == 5:
                await message.bot.delete_message(message.from_user.id, int(message['message_id']))
                await message.bot.send_message(message.from_user.id, "🔙 Возвращаемся в главное меню",
                                               reply_markup=markup)
                count = 0
        else:
            try:
                await message.bot.send_message(message.from_user.id, "Ошибка", reply_markup=markup)
                count = 0

            except:
                await message.bot.send_message(admin_id, "Там у кого-то ошибка", reply_markup=markup)

    else:
        msg_kan = 'Для использования бота, пожалуйста, подпишитесь на канал' + '\n\n' + 'https://t.me/goodmood_kanal'
        await message.bot.send_message(message.from_user.id, msg_kan, reply_markup=markup_podpisk)
    print('count_2 = ', count)
    print('-----------------------------')
