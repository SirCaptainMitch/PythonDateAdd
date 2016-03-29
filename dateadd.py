"""
Attempting to recreate the MSSQL DATEADD function in python 3

 returns to / formatting: _datetime.strptime(date,"%m/%d/%Y").strftime('%m/%d/%Y')
"""

from datetime import datetime as _datetime
from datetime import timedelta as _timedelta
import calendar as _calendar


__datepart__ = ['m','y','d','month','day','year']
__date__ = ['datetime.datetime','datetime','str']


def __verifyIncrement(inc):
    return isinstance(inc, int)


def __verifyDate(date):
    return type(date).__name__ in __date__


def __verifyDatePart(datepart):
    if type(datepart).__name__ != 'str' or datepart not in __datepart__:
        return False
    else:
        return True


def __add_months(inc, date):
    # if months > 12 then need to adjust the year as well.
    add = date.month - 1 + inc
    year = int(date.year + add / 12 )
    # In order to properly handle negative increments, keep adding 12 until the month is > 1
    # jan = 1 , nov = 11 inc = -2
    # (1 - (-2) ) + 12 = 11
    month = ((date.month % 12) + inc) % 12
    # no month can be 0, so 0 = 12.
    if month == 0:
        month = 12

    day = min(date.day,_calendar.monthrange(year,month)[1])
    retdate = _datetime(year=year, month=month, day=day)

    return retdate

def __add_years(inc, date):
    # years don't impact months or days. Simple addition.
    year = int(date.year + inc)
    month = date.month
    day = min(date.day,_calendar.monthrange(year,month)[1])

    retdate = _datetime(year=year, month=month, day=day)

    return retdate

def __add_days(inc, date):
    # timedelta handles days, even negatives.
    retdate = date + _timedelta(days=inc)
    return retdate


def dateadd(datepart, inc, date):
    if not all((__verifyDatePart(datepart.lower()), __verifyIncrement(inc), __verifyDate(date))):
        return 'it\'s wrong.'
    else:
        # make sure date is either in m/d/y or d/m/y format the convert to datetime type
        if type(date).__name__ == 'str':
            try:
                date = _datetime.strptime(date,"%m/%d/%Y")
            except ValueError:
                try:
                    date = _datetime.strptime(date,"%d/%m/%Y")
                except ValueError:
                    print('Please format the date string as m/d/y or d/m/y')

        if datepart.lower() in ['m','month']:
            return __add_months(inc, date)

        if datepart.lower() in ['d','day']:
            return __add_days(inc, date)

        if datepart.lower() in ['y','year']:
            return __add_years(inc,date)

