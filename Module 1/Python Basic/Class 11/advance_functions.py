# DECORATORS
def change_case(func): # DECORATOR FUNCTION
    def mylower():
        return func().lower()
    return mylower()

@change_case
def myfunction(): # BASE FUNCTION
    return 'Hello World'
print(myfunction)

@change_case
def hisfunction():
    return 'CLASS 11'
print(hisfunction)

@change_case
def herfunction():
    return 'SAYLANI TECH LIMITED'
print(herfunction)

# DECORATOR WITH ARGUMENTS
def greeting(func):
    def inner(x):
        return 'HELLO '+str(x)
    return inner

@greeting
def theirfunc(name):
    return name

print(theirfunc('Uzair'))


# LAMBDA FUNCTION
# MANY ARGUMENTS BUT ONE EXPRESSION
x = lambda a:a+10
print(x(20))

# MULTIPLE ARGUMENTS
y = lambda a,b: a+b
print(y(44, 51))


z = lambda a,b: 'HELLO '+a+' and '+b
print(z('Ayan', 'Ibrahim'))

#FUNCTION USE CASE
def myfunc(num):
    return lambda a:a+num

myadder = myfunc(20)
print(type(myadder))
print(myadder(40))


# RECURSION
def countdown(n):
    if n<=0:
        return 'DONE'
    else:
        print(n)
        countdown(n-1)
        
print(countdown(10))

# FACTORIAL
def factorial(n):
    # BASE CASE
    if n==0 or n==1:
        return 1
    # RECURSIVE CASE
    else:
        return n * factorial(n-1)




