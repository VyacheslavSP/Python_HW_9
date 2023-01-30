#!/usr/bin/python
import datetime
import ephem

answer = None


def get_phase_on_day():
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    date = ephem.Date(datetime.date(year, month, day))

    nnm = ephem.next_new_moon(date)
    pnm = ephem.previous_new_moon(date)

    lunation = (date-pnm)/(nnm-pnm)
    if (lunation == 0):
        answer = "Новолуние"
    elif (0 < lunation <= 0.125):
        answer = "Молодая луна"
    elif (0.125 < lunation <= 0.25):
        answer = "Первая четверть"
    elif (0.25 < lunation <= 0.375):
        answer = "Прибывающая луна"
    elif (0.375 <= lunation <= 0.5):
        answer = "Полнолуние"
    elif (0.5 < lunation <= 0.625):
        answer = "Убывающая луна"
    elif (0.625 < lunation <= 0.75):
        answer = "Последняя четверть "
    else:
        answer = "Старая луна."

    return answer
