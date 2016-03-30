# PythonDateAdd

Adds the functionality of the T-SQL DATEADD function to python making use of datetime, calendar and timedelta. 

I was writing a script to check file created dates and noticed that it was rather tedius to add or subtract a number to a date. However it was rather easy to accomplish this in SQL. So I figured why not build it? 

As of right now it will do Years, Days and Months. I plan to add Weeks, Hours, Minutes, Seconds, and Milliseconds.

The example syntax is as follows:

Import the dateadd function from the dateadd module.

The function parameters are: dateadd(Datepart, increment, date)

Dateadd: ('m','d','y','month','day','year')
Increment: positive or negative
Date: datetime and string types in M/D/Y or D/M/Y format.

print(dateadd('m',-1,'03/30/2016'))

Should return: 02/29/2016


