from datetime import datetime
import datetime

c = [[1, 2, 3, 4, 5, 5], [4, 5, 3], [5], [], [], [], [1, 3]]
n = 5
mass = [[], [], [], [], [], [], []]
mass_week_days = [[' <b>Понедельник</b> - '], [' <b>Вторник</b> - '], [' <b>Среда</b> - '], [' <b>Четверг</b> - '], [' <b>Пятница</b> - '], [' <b>Суббота</b> - '], [' <b>Воскресенье</b> - ']]

# time = 2021-12-17
# now = datetime.now()
# t = now.strftime("%w")

def draw_table(week_records, count):
    week_mood = [[], [], [], [], [], [], []]
    for i in range(0, len(week_records)):

        rec = week_records[i]
        if int(rec[4]) == 1:
            week_mood[0].append(int(rec[2]))
        if int(rec[4]) == 2:
            week_mood[1].append(int(rec[2]))
        if int(rec[4]) == 3:
            week_mood[2].append(int(rec[2]))
        if int(rec[4]) == 4:
            week_mood[3].append(int(rec[2]))
        if int(rec[4]) == 5:
            week_mood[4].append(int(rec[2]))
        if int(rec[4]) == 6:
            week_mood[5].append(int(rec[2]))
        if int(rec[4]) == 0:
            week_mood[6].append(int(rec[2]))

    print(week_mood)



    msg = 'Записи \n'
    time = datetime.date.today()
    week_day = int(time.strftime("%w"))
    for i in range(1, 8):
        day_date = time + datetime.timedelta(days= i - week_day)
        mass[i-1].append(str(day_date))
        msg = msg + str(day_date)
        mass[i-1].append(str(mass_week_days[i-1][0]))
        msg = msg + str(mass_week_days[i-1][0])
        for j in range(0, int(count)):
              try:
                  mass[i-1].append(str((week_mood[i-1])[j]))
                  msg = msg + str((week_mood[i-1])[j])
                  mass[i-1].append('/')
                  msg = msg + '/'
              except:
                  if day_date <= time:
                        mass[i - 1].append('❌')
                        msg = msg + '❌'
                        mass[i - 1].append('/')
                        msg = msg + '/'
                  else:
                        mass[i - 1].append('⚪')
                        msg = msg + '⚪'
                        mass[i - 1].append('/')
                        msg = msg + '/'

        mass[i - 1].append(' \n')
        msg = msg + ' \n'
        print(mass[i-1])
    print(msg)

    print(time, week_day)
    return msg

