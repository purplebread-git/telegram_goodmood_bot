import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_count(self):
        ''' Количество пользователей'''
        self.cursor.execute("select count(*) from `users`")
        return self.cursor.fetchone()

    def update_daily_count(self, dev_id, value):

        sql_update_query = """Update users set daily_count = ? where id = ?"""
        data = (value, dev_id)
        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        print("Запись успешно обновлена")



    def get_user_id(self, user_id):
        """Достаем id юзера в базе по его user_id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем юзера в базу"""
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_record(self, user_id, value):
        """Создаем запись о доходах/расходах"""
        self.cursor.execute("INSERT INTO `records` (`users_id`, `value`) VALUES (?,?)",
            (self.get_user_id(user_id), value))
        return self.conn.commit()

    def get_records(self, user_id, within = "all"):
        """Получаем статистику"""

        if(within == "year"):
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "week"):
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'localtime', 'weekday 1', '-7 days') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        elif(within == "month"):
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? AND `date` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date`",
                (self.get_user_id(user_id),))
        else:
            result = self.cursor.execute("SELECT * FROM `records` WHERE `users_id` = ? ORDER BY `date`",
                (self.get_user_id(user_id),))

        return result.fetchall()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()