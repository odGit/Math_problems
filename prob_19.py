# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:13:37 2013

@author: olgis

Problem: 
    How many Sundays fell on the first of the month
    during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    
IMPORTANT:
    1 Jan 1900 was a Monday.
    January, March, May, July, August, October, December has 31 day.
    April, June, September November has 30 day.
    February has 28 and 29 on leap years.
    A leap year is any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

"""

import datetime
import time

dict_months = {"Jan":1,"Feb":2,"Mar":3, "Apr":4, "May":5, "June":6,
               "July":7, "August":8, "September":9, "October":10,
               "November":11,"December":12}
               
dict_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,10:31,
             11:30, 12:31}
dict_week = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4,
             "Saturday":5, "Sunday":6}

def read_date(my_date):
    for d in my_date.split():
        if d.isdigit():
            if len(d) > 2: year = int(d)
            else: day = int(d)
        else:
            month = d
    return [day, month, year]

def count_days(start_date, end_date, week_day, date):
    res = 0
    str_day, str_month, str_year = read_date(start_date)
    end_day, end_month, end_year = read_date(end_date)
    w_day = dict_week[week_day]
    length = (end_year - str_year) + 1
    for year in xrange(length, 0, -1):
        for month in xrange(1,13):
            d = datetime.date(1900 + year, month, 1)
            if (d.weekday() == w_day): res += 1
            
    return res


start = time.time()
product = count_days("1 Jan 1901", "31 Dec 2000", "Sunday", 1)  
elapsed = time.time() - start     

print "The answer is %s, it took %s sec"  %(product, elapsed)     