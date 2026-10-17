name = 'Irtiza' # STRING
age = 22 # INTEGER

# F Strings (Stings Formatting)
print('My name is Irtiza and my age is 22')
print('My name is '+ name+' and my age is '+str(age))
print('My name is', name, 'and my age is', age)
# F Strings
print(f'My name is {name} and my age is {age}')



# ESCAPE SEQUENCES \
# print('My name is 'Irtiza' and my age is 22')
print("My name is 'Irtiza' and my age is 22")
print('My name is "Irtiza" and my age is 22')
# \' \"
print('My name is \'Irtiza\' and my age is 22') # Best Practice
print('My name is Irtiza and my age is 22')
print('My name is /Irtiza\ and my age is 22')
# \\
print("My name is Irtiza\\ and my age is 22")
# \n (new line)
print('\nMy name is Irtiza and\n my age is 22')
# \t (tab spacing)      
print('My name is Irtiza\tmy age is 22')
# \b (Backspace)
print('My name is \b\b\bIrtiza a\bnd my age is 22') # Removed 3 characters back from Irtiza and 1 character from n in and

import os
os.system('cls')

# STRINGS METHODS
# find -> returns the starting position
txt = 'My name is Irtiza and my age is 22'

print(txt.find('and'))
print(txt[18:])
# find is case sensitive my and My are different
print(txt.find('My'))
# rfind searches from last
print(txt.rfind('is'))

# split
print(txt.split(' '))
print(txt.split('and'))
# strip
print(txt.split('and')[1].strip())




