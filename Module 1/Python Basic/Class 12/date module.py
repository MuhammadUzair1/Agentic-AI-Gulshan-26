"""
================================================================
 Module 1 - Python Basics | Class 12 (Part 1): The datetime Module
================================================================

Python does not have a special "date" data type built in.
Instead, we use the built-in module called 'datetime'.

It lets us:
    - get today's date and the current time
    - create any date we want (e.g. a date of birth)
    - show dates in different formats (21/11/2026, 21-Nov-2026 ...)
    - do maths with dates (age, days left until Eid, due dates ...)

Topics covered in this file:
    1. Importing datetime
    2. The current date and time - now()
    3. Getting parts of a date: year, month, day, hour ...
    4. Creating your own date
    5. Formatting dates - strftime()
    6. Converting text into a date - strptime()
    7. Date maths - subtracting dates and timedelta
    8. Practice examples

NOTE: The outputs in the comments are examples. Your output will
show YOUR current date and time.
"""


# ==============================================================
# 1. IMPORTING datetime
# ==============================================================
# The module is called 'datetime', and inside it there is a
# CLASS that is ALSO called 'datetime'. That's why you will often see:
#
#     import datetime                  -> use as datetime.datetime.now()
#     from datetime import datetime    -> use as datetime.now()   (shorter)
#
# We will use the shorter way, with a few other helpers too:

from datetime import datetime, date, timedelta


# ==============================================================
# 2. THE CURRENT DATE AND TIME - now()
# ==============================================================
now = datetime.now()

print(now)              # 2026-11-21 14:35:12.123456
print(now.date())       # 2026-11-21     (only the date)
print(now.time())       # 14:35:12.123456 (only the time)

# date.today() gives only today's date
print(date.today())     # 2026-11-21
print()


# ==============================================================
# 3. GETTING PARTS OF A DATE
# ==============================================================
print('Year  :', now.year)          # 2026
print('Month :', now.month)         # 11
print('Day   :', now.day)           # 21
print('Hour  :', now.hour)          # 14  (24-hour clock)
print('Minute:', now.minute)        # 35
print('Second:', now.second)        # 12

# weekday() -> Monday = 0, Tuesday = 1 ... Sunday = 6
print('Weekday number:', now.weekday())

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('Today is', days[now.weekday()])
print()


# ==============================================================
# 4. CREATING YOUR OWN DATE
# ==============================================================
# datetime(year, month, day, hour, minute, second)
# Only year, month and day are required. The rest default to 0.

dob = datetime(2005, 12, 31)
print(dob)                          # 2005-12-31 00:00:00

class_time = datetime(2026, 11, 26, 19, 30)
print(class_time)                   # 2026-11-26 19:30:00

# Python checks if the date is real:
# datetime(2026, 2, 30)  -> ValueError: day is out of range for month
print()


# ==============================================================
# 5. FORMATTING DATES - strftime()
# ==============================================================
# strftime = "STRing FROM TIME" -> turns a date into TEXT
# in any format you like, using these codes:
#
#   | Code | Meaning                 | Example   |
#   |------|-------------------------|-----------|
#   | %d   | Day (01-31)             | 21        |
#   | %m   | Month number (01-12)    | 11        |
#   | %b   | Month name (short)      | Nov       |
#   | %B   | Month name (full)       | November  |
#   | %y   | Year (2 digits)         | 26        |
#   | %Y   | Year (4 digits)         | 2026      |
#   | %a   | Weekday (short)         | Sat       |
#   | %A   | Weekday (full)          | Saturday  |
#   | %H   | Hour (00-23)            | 14        |
#   | %I   | Hour (01-12)            | 02        |
#   | %M   | Minute (00-59)          | 35        |
#   | %S   | Second (00-59)          | 12        |
#   | %p   | AM / PM                 | PM        |
#
# Anything that is NOT a code (like / - , : or spaces) is printed as it is.

print(now.strftime('%d%m%y'))           # 211126
print(now.strftime('%d%m%Y'))           # 21112026
print(now.strftime('%d-%m-%y'))         # 21-11-26
print(now.strftime('%d/%m/%Y'))         # 21/11/2026
print(now.strftime('%d %b %Y'))         # 21 Nov 2026
print(now.strftime('%d %B %Y'))         # 21 November 2026
print(now.strftime('%A, %d %B %Y'))     # Saturday, 21 November 2026
print(now.strftime('%I:%M %p'))         # 02:35 PM
print(now.strftime('%H:%M:%S'))         # 14:35:12
print()


# ==============================================================
# 6. CONVERTING TEXT INTO A DATE - strptime()
# ==============================================================
# strptime = "STRing PARSE TIME" -> the OPPOSITE of strftime.
# It turns TEXT into a real date. You must tell Python the format.
#
#   strftime: date  ---> text
#   strptime: text  ---> date

text = '14/08/1947'
independence_day = datetime.strptime(text, '%d/%m/%Y')
print(independence_day)                             # 1947-08-14 00:00:00
print(independence_day.strftime('%A'))              # Thursday

meeting = datetime.strptime('2026-12-25 10:30', '%Y-%m-%d %H:%M')
print(meeting)                                      # 2026-12-25 10:30:00
print()


# ==============================================================
# 7. DATE MATHS - SUBTRACTING DATES AND timedelta
# ==============================================================
# Subtracting two dates gives a 'timedelta' (a DIFFERENCE in time)

date1 = datetime(2005, 12, 31)
date2 = datetime(2009, 12, 18)
difference = date2 - date1

print(difference)                   # 1448 days, 0:00:00
print(difference.days)              # 1448
print(type(difference))             # <class 'datetime.timedelta'>

# timedelta lets us ADD or SUBTRACT time from a date
today = datetime.now()
print('Today       :', today.strftime('%d %b %Y'))
print('In 10 days  :', (today + timedelta(days=10)).strftime('%d %b %Y'))
print('2 weeks ago :', (today - timedelta(weeks=2)).strftime('%d %b %Y'))
print('In 3 hours  :', (today + timedelta(hours=3)).strftime('%I:%M %p'))
print()


# ==============================================================
# 8. PRACTICE EXAMPLES
# ==============================================================

# --- Age calculator ---
birthday = datetime(2000, 5, 15)
age_in_days = (datetime.now() - birthday).days
print('You are', age_in_days, 'days old')
print('That is about', age_in_days // 365, 'years')
print()

# --- Days left until the new year ---
next_year = datetime(datetime.now().year + 1, 1, 1)
days_left = (next_year - datetime.now()).days
print('Days left until', next_year.year, ':', days_left)
print()

# --- Library book due date (14 days from today) ---
issued = datetime.now()
due = issued + timedelta(days=14)
print('Book issued on:', issued.strftime('%d/%m/%Y'))
print('Return it by  :', due.strftime('%A, %d %B %Y'))
print()

# --- Good morning / afternoon / evening ---
hour = datetime.now().hour
if hour < 12:
    print('Good Morning!')
elif hour < 17:
    print('Good Afternoon!')
else:
    print('Good Evening!')
