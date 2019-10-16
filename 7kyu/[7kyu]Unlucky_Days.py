'''
Unlucky Days
https://www.codewars.com/kata/unlucky-days/python

Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.
'''

import calendar

def unlucky_days(year):
    
    count = 0 #counting the number of Friday 13ths
    
    for month in range(1,13):
        weekday = calendar.weekday(year,month,13)
        if weekday == 4: #Friday
            count+=1
            
    return count
