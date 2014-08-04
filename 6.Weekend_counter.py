#!/usr/bin/python

from datetime import date
from itertools import cycle

def checkio(from_date, to_date):
    """ Takes in two dates and returns the count of weekend days """
    daystring = "0123456"
    no_days = abs(to_date - from_date).days
    cur_day = from_date.weekday()
    split_days = daystring.split(str(cur_day))
    cur_daystring = str(cur_day)+split_days[1]+split_days[0]
    day_count = 0
    count = 0
    for cur_day in cycle(cur_daystring):
        if cur_day in ('5','6'):
            count = count + 1
        if day_count == int(no_days):
            break        
        day_count = day_count + 1
    return count 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
