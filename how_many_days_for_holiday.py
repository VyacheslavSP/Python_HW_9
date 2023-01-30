import datetime


def how_many():

    day_of_holiday_year = datetime.date.today().year
    date_of_holyday = datetime.date(day_of_holiday_year, 12, 31)
    holiday_day = (date_of_holyday-datetime.date.today())
    result = str(int((str(holiday_day).split())[0])+1)
    return (result)
