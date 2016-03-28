"""
Attempting to recreate the MSSQL DATEADD function in python 3


 print('The increment {0} is not an int, it is a {1}'.format(inc, type(inc).__name__))
 print('The Datepart {0} is not a string, it is a {1}'.format(datepart, type(datepart).__name__))
 print('The date {0} is not a date, it is a {1}'.format(date, type(date).__name__))

 returns to / formatting: _datetime.strptime(date,"%m/%d/%Y").strftime('%m/%d/%Y')
"""

from datetime import datetime as _datetime
from datetime import timedelta as _timedelta
import calendar as _calendar


__datepart__ = ['m','y','d','month','day','year']
__date__ = ['datetime.datetime','datetime','str']


def __verifyIncrement(inc):
    if type(inc).__name__ != 'int':
        return False
    else:
        return True


def __verifyDate(date):
    if type(date).__name__ not in __date__:
        return False
    else:
        return True


def __verifyDatePart(datepart):
    if type(datepart).__name__ != 'str' or datepart not in __datepart__:
        return False
    else:
        return True


def __add_months(inc, date):
    ## Months are weird and I do not like them.
    add   = date.month - 1 + inc
    year  = int(date.year + add / 12 )
    month = date.month % 12 + inc

    while month < 1:
        month = month + 12

    day = min(date.day,_calendar.monthrange(year,month)[1])
    retdate = _datetime(year=year, month=month, day=day)

    return retdate

def dateadd(datepart, inc, date):
    if __verifyDatePart(datepart.lower()) == False or __verifyIncrement(inc) == False or __verifyDate(date) == False:
        return 'it\'s wrong.'
    else:
        if type(date).__name__ == 'str':
            date = _datetime.strptime(date,"%m/%d/%Y")

        if datepart.lower() in ['m','month','Month']:
            return __add_months(inc, date)



        if datepart.lower() in ['d','day']:
            if inc >= 0:
                retdate = date + _timedelta(days=inc)
                return retdate
            else:
                retdate = date - _timedelta(days=abs(inc))
                return retdate

        # if datepart in ['y','year']:
        #     if inc >= 0:
        #         retdate = date + _timedelta(days=inc)
        #     else:
        #         retdate = date - _timedelta(days=abs(inc))
