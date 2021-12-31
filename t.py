from datetime import datetime
import datetime
"""
today = datetime.datetime.now().replace(day=1)
monday = today - datetime.timedelta(days=today.weekday())
today = today.strftime("%Y-%m-%d %H:%M:%S")
monday = monday.strftime("%Y-%m-%d")
monday = "{0} {1}".format(monday, "00:00:00")
week_mood = [[], [], [], [], [], [], []]
print(today)
print(monday)"""

a = [{'id': 15, 'users_id': 4, 'value': ('3'), 'date': datetime.datetime(2021, 12, 3, 1, 52, 9)}]
a = a[0]['date'].strftime('%d')
if a == '03':
    print(a[0]['date'][0])
print(a)