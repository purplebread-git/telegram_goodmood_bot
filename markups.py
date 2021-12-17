from aiogram import types


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("➕ Добавить запись")
item2 = types.KeyboardButton("📊  Статистика")
item3 = types.KeyboardButton("⚙️Настройки")
markup.add(item1, item2, item3)

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица админа -.-.-.-.-.-.-.-.-.-.-.-.-

markup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Отправить всем сообщение")
item2 = types.KeyboardButton("Кол-во пользователей")
item3 = types.KeyboardButton("🔙 Назад")
markup_admin.add(item1, item2, item3)

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица выбора настроения -.-.-.-.-.-.-.-

markup_mood = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton(" 😀 ", callback_data='nice')
item2 = types.KeyboardButton(" 🙂 ", callback_data='good')
item3 = types.KeyboardButton(" 😕 ", callback_data='-')
item4 = types.KeyboardButton(" 😔 ", callback_data='bad')
item5 = types.KeyboardButton(" 😭 ", callback_data='verybad')
item6 = types.KeyboardButton("🔙 Назад", callback_data='back')
markup_mood.add(item1, item2, item3, item4, item5, item6)

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица проверки подписки -.-.-.-.-.-.-.-

markup_podpisk = types.InlineKeyboardMarkup(resize_keyboard=True)
item1 = types.InlineKeyboardButton("Подписаться", callback_data='link_podpisk', url='https://t.me/goodmood_kanal')
item2 = types.InlineKeyboardButton("✅ Я подписался", callback_data='podpisk')
markup_podpisk.add(item1, item2)

# -.-.-.-.-.-.-.-.-.-.-.-.- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

markup_start = types.InlineKeyboardMarkup(resize_keyboard=True)
item1 = types.InlineKeyboardButton("✅ Я подписался", callback_data='ready')
markup_start.add(item1)

# -.-.-.-.-.-.-.-.-.-.-.-.- -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("🔙 Назад")
markup_back.add(item1)


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