import pymysql
from config import host, db_name, db_user, db_pass
import datetime
class BotDB():

    def __init__(self):

        try:
            self.conn = pymysql.connect(host=host,
                                  user=db_user,
                                  password=db_pass,
                                  database=db_name,
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

            self.cur = self.conn.cursor()
            print('Подключение к БД произошло успешно')
        except:
            print('Ошибка в подключении к БД')

    """Проверяем, есть ли юзер в базе"""
    def user_exists(self, user_id):
        self.cur.execute("SELECT `id` from `users` WHERE `user_id` = {0}".format(user_id))
        print('1')
        a = self.cur.fetchall()
        print(a)
        if a == tuple():
            return tuple()
        else:
            return a[0]['id']

    ''' Количество пользователей'''
    def get_count(self):
        self.cur.execute("select count(*) from `users`")
        return self.cur.fetchone()

    """Обновление количества напоминалок"""
    def update_daily_count(self, dev_id, value):

        sql_update_query = "Update users set daily_count = {0} where id = {1}".format(value, dev_id)
        self.cur.execute(sql_update_query)
        self.conn.commit()

        print("Запись успешно обновлена")

    """Достаем id юзера в базе по его user_id"""
    def get_user_id(self, user_id):

        result = self.cur.execute("SELECT `id` FROM `users` WHERE `user_id` = {0}".format(user_id))
        return self.cur.fetchone()['id']

    """Добавляем юзера в базу"""
    def add_user(self, user_id):

        self.cur.execute("INSERT INTO `users` (`user_id`) VALUES ({0})".format(user_id))
        print("Добавляем юзера в базу")
        return self.conn.commit()

    """Создаем запись """
    def add_record(self, user_id, value):

        self.cur.execute("INSERT INTO `records` (`users_id`, `value`) VALUES ({0}, {1})".format(self.get_user_id(user_id), value))
        return self.conn.commit()

    """Получаем статистику"""
    def get_records(self, user_id, within="all"):


        if within == "year":

            result = self.cur.execute(
                "SELECT * FROM `records` WHERE `users_id` = {0} AND `date` BETWEEN datetime('now', 'start of year') AND datetime('now', 'localtime') ORDER BY `date`".format(self.get_user_id(user_id)))
        elif within == "week":
            today = datetime.datetime.now()
            monday = today - datetime.timedelta(days=today.weekday())
            today = today.strftime("%Y-%m-%d %H:%M:%S")
            monday = monday.strftime("%Y-%m-%d")
            monday = "{0} {1}".format(monday, "00:00:00")
            stroke = """SELECT * FROM `records` WHERE `users_id` = {0} AND `date` BETWEEN {3}{1}{4} AND {5}{2}{6} ORDER BY `date`""".format(self.get_user_id(user_id), monday, today, '"', '"','"','"',)
            self.cur.execute(stroke)
            return self.cur.fetchall()

        elif within == "month":
            day_start = datetime.datetime.now().replace(day=1)
            day_start = day_start.strftime("%Y-%m-%d")
            day_start = "{0} {1}".format(day_start, "00:00:00")
            try:
                day_over_month = datetime.datetime.now().replace(day=31).strftime("%Y-%m-%d")
            except:
                try:
                    day_over_month = datetime.datetime.now().replace(day=30).strftime("%Y-%m-%d")
                except:
                    day_over_month = datetime.datetime.now().replace(day=29).strftime("%Y-%m-%d")
            day_over_month = "{0} {1}".format(day_over_month, "00:00:00")

            stroke = """SELECT * FROM `records` WHERE `users_id` = {0} AND `date` BETWEEN {3}{1}{4} AND {5}{2}{6} ORDER BY `date`""".format(
                self.get_user_id(user_id), day_start, day_over_month, '"', '"', '"', '"', )
            self.cur.execute(stroke)
            return self.cur.fetchall()

        else:
            result = self.cur.execute("SELECT * FROM `records` WHERE `users_id` = {0} ORDER BY `date`".format(self.get_user_id(user_id)))
            return self.cur.fetchall()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()