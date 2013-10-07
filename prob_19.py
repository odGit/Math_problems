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

SOLUTION:
    1. Count how many days are between START_DATE and END_DATE
    2. Assign week days to them
    3. select every 1st if it is Mondays.
"""

import time
import sys

dict_months = {"Jan":1,"Feb":2,"Mar":3, "Apr":4, "May":5, "June":6,
               "July":7, "August":8, "September":9, "October":10,
               "November":11,"December":12}
               
dict_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,10:31,
             11:30, 12:31}
                
def read_date(my_date):
    for d in my_date.split():
        if d.isdigit():
            if len(d) > 2:
                year = int(d)
            else:
                day = int(d)
        else:
            month = d
            
    return [day, month, year]


def count_days(date1, date2):
    #extract from string date
    start_day, start_month, start_year = read_date(date1)
    end_day, end_month, end_year = read_date(date2)
    #convert months in to digits
    start_month = dict_months[start_month]
    end_month = dict_months[end_month]

    if start_year == end_year:
        
        if start_month == end_month: #within the same month
            days_num = end_day - start_day + 1
        else:
            days_num = dict_days[start_month] - start_day + 1 #+1 for start date the start_Date
            print days_num
            if start_month + 1 == end_month:
                days_num += end_day
            else:
                for x in xrange(end_month, start_month, -1):
                    if x == 2 and start_year % 4 == 0:
                        days_num += 1
                    days_num += dict_days[x]
    


start = time.time()
product = count_days("27 Jan 1901","3 Feb 1901")
elapsed = time.time() - start