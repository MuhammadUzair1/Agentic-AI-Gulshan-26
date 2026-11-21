import datetime
from datetime import datetime as dt

now = datetime.datetime.now()
print(now)

print(now.time())
print(now.date())

print(now.date().year)
print(now.date().weekday())

# DATE FORMATS
print(now.strftime('%d%m%y')) #211126
print(now.strftime('%d%m%Y')) #21112026
print(now.strftime('%d%b%y')) #21Nov26
print(now.strftime('%d-%m-%y')) #21-11-26
print(now.strftime('%d%B%y')) #21November26
print(now.strftime('%d/%m/%y')) #21/11/26
print(now.strftime('%d%m')) #21/11/26


# DATE CREATION
dob = dt(2005,12,31)
print(dob)

# DATE OPERATIONS
date = dt(2009,12,18)
print((date - dob).days)