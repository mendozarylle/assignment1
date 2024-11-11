#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Rylle Mendoza
Semester: Fall2024
Description: <fill this in>
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return true if the year is a leap year"
    # A year is a leap year if it is divisible by 4 but not by 100,
    # except if it is also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    # Months with 31 days
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Months with 30 days
    elif month in [4, 6, 9, 11]:
        return 30
    # February: check if it's a leap year
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    return 0

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    if day > mon_max(mon, year):
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "Check validity of date"
    try:
        day, mon, year = map(int, date.split('/'))
        if mon < 1 or mon > 12:
            return False
        if day < 1 or day > mon_max(mon, year):
            return False
        return True
    except ValueError:
        return False

def day_iter(start_date: str, num: int) -> str:
    "Iterates from start date by num to return end date in DD/MM/YYYY"
    date = start_date  # Starts with the initial date
    for _ in range(abs(num)):
        # Determines the direction of date change: forward for positive `num`, backward for negative
        date = after(date) if num > 0 else before(date)
    return date  # Returns the final date after iterating

if __name__ == "__main__":
    # Ensures the user provides exactly 3 arguments; if not, shows usage instructions
    if len(sys.argv) != 3:
        usage()  
    
    start_date = sys.argv[1]  # First argument should be the starting date
    try:
        # Converts the second argument to an integer to check if it represents a valid number of days
        num_days = int(sys.argv[2])
    except ValueError:
        usage()  # If the second argument isn’t a number, show usage instructions
    
    # Validates the format and values of the provided start date
    if not valid_date(start_date):
        usage()  # Show usage instructions if the date is invalid
    
    # Calculates the end date by iterating from the start date by `num_days`
    end_date = day_iter(start_date, num_days)
    # Outputs the end date with its corresponding day of the week
    print(f"The end date is {day_of_week(end_date)}, {end_date}.")
