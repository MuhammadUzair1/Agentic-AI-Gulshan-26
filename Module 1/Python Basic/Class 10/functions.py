# FUNCTIONS
# They provide reusability
# They provide easy maintanence
# They provide clean code

# FUNCTION DEFINATION
# ACTUAL CODE SNIPPET OF FUNCTION
'''
SYNTAX
python keyword 'def' is used to create funciton
def function name()

'''

# FUNCTION DEFINATION
def this_function():
    print('THIS IS A FUNCTION')
    
# FUNCTION CALL
this_function()
this_function()


# FUNCTION TO CONVERT FAHRENITE TO CELCIUS
num = 100
def temp_f_to_c():
    calc = (num -32) *5/9
    print(calc)
    
temp_f_to_c()

# PARAMETERS
def f_2_c(num):
    calc = (num -32) *5/9
    print(calc)
    
f_2_c(102)

# MUTLIPLE PARAMETERS
def area(l,b):
    print(l*b)

f_2_c(105)

area(5,5)

# ORDERING IN PARAMETERS IS IMP
def salary_calc(amount, tax, allowance):
    gross_sal = amount + allowance
    net_sal = gross_sal - gross_sal*tax/100
    print(net_sal)
    
salary_calc(200, 10, 50)

# WRONG RESULT
salary_calc(4500000, 4500, 15) # ORDERING WRONG

# USING PARAMETERS NAMES TO ASSIGN VALUES
salary_calc(allowance=45000, tax=10, amount=450000)

# RETURNING VALUES
def is_vowel(letter):
    if letter.lower() in ['a','e','i','o','u']:
        return 'IS VOWEL'
    else:
        return 'IS NOT VOWEL'

value = is_vowel('z')
print(value)

# EMPTY FUNCTIONS
def empty_function():
    pass

# PARAMETERS VS ARGUMENTS
def full_name(fname, lname): # fname, lname -> parameters
    return (fname + ' ' + lname)

print(full_name('Muhammad', 'Uzair')) # Muhammad Uzair -> arguments


# DEFAULT ARGUMENTS
# IF NO INPUT AT CALL THEN USE THIS VALUE
def full_name_def(fname, lname = 'Khan'):
    return (fname + lname)

print(full_name_def('Uzair'))


# TYPE CAST
def full_name_def2(fname, lname = 'Khan'):
    return (str(fname) + str(lname))

val=full_name_def2(1,2)
print(val)

# *args
# WHEN WE DON'T KNOW NUMBER OF ARGUMENTS
def my_func(*fruit):
    print('The best fruit is: ', fruit[3])

my_func('apple','banana','mango','grape','watermelon','orange')

def greets(*name,greetings ):
    for i in name:
        print(greetings, i)
        
greets('Ibrahim', 'Uzair','Irtiza', 'Maaz', 'Owais', 'Moiz', 'Saif','Shahid','Huzaifa', greetings='Assalam Alaikum')        


# **kwargs
def intro(**myself):
    print('My name is', myself['name'], 'I am a', myself['work'])
    
intro(name = 'Uzair Khan', work = 'Data Engineer', age = 26)

# SCOPE OF VARIABLES
z = 400 # GLOBAL VARIABLE
def myfunc():
    x = 200 # LOCAL VARIABLE
    def printfunc():
        print(x)
        print(z)
    printfunc()
    
myfunc()





