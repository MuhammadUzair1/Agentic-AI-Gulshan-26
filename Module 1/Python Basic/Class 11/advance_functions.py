"""
================================================================
 Module 1 - Python Basics | Class 11 (Part 1): Advanced Functions
================================================================

In Class 10 we learned how to create and call normal functions.
Now we will learn some more powerful things we can do with them.

Remember: in Python a function is also a VALUE (like a number or
a string). This means we can:
    - store a function in a variable
    - pass a function to another function
    - return a function from another function
Everything in this file is built on that idea.

Topics covered in this file:
    1. Functions are values (warm-up)
    2. Decorators              - add extra behaviour to a function
    3. Decorators with arguments (*args, **kwargs)
    4. Lambda functions        - small one-line functions
    5. Lambda with sorted(), map() and filter()
    6. A function that returns a function
    7. Recursion               - a function that calls itself
    8. Practice examples
"""


# ==============================================================
# 1. FUNCTIONS ARE VALUES (WARM-UP)
# ==============================================================
def say_hello():
    return 'Hello!'

# WITH brackets ()    -> the function RUNS and gives back its result
# WITHOUT brackets    -> we are talking about the function ITSELF
print(say_hello())      # Hello!
print(say_hello)        # <function say_hello at 0x...>

# We can store a function in another variable and call it from there
greet = say_hello
print(greet())          # Hello!
print()


# ==============================================================
# 2. DECORATORS
# ==============================================================
# A DECORATOR is a function that WRAPS another function to add
# some extra behaviour, WITHOUT changing the original code.
#
# Think of a gift:  the gift = your function
#                   the wrapping paper = the decorator
# The gift is the same, but now it has something extra around it.
#
# Structure of a decorator:
#
#   def decorator(func):          # 1. receives a function
#       def wrapper():            # 2. creates a new "wrapper" function
#           ... extra work ...
#           result = func()       # 3. calls the original function
#           ... extra work ...
#           return result
#       return wrapper            # 4. returns the wrapper (NO brackets!)

def change_case(func):              # DECORATOR FUNCTION
    def wrapper():
        result = func()             # run the original function
        return result.lower()       # extra work: make it lowercase
    return wrapper                  # return the function, don't call it


@change_case                        # same as: my_function = change_case(my_function)
def my_function():                  # BASE FUNCTION
    return 'Hello World'

@change_case
def his_function():
    return 'CLASS 11'

@change_case
def her_function():
    return 'SAYLANI TECH LIMITED'

print(my_function())        # hello world
print(his_function())       # class 11
print(her_function())       # saylani tech limited
print()


# --- What does the @ symbol actually do? ---
# These two blocks do EXACTLY the same thing:
#
#   @change_case                     def shout():
#   def shout():                         return 'HEY'
#       return 'HEY'                 shout = change_case(shout)
#
# '@' is just a short and clean way of writing it.


# --- A decorator that prints messages before and after ---
def announce(func):
    def wrapper():
        print('>>> Starting...')
        func()
        print('>>> Finished!')
    return wrapper

@announce
def make_tea():
    print('    Boiling water, adding tea leaves and milk')

make_tea()
print()


# ==============================================================
# 3. DECORATORS WITH ARGUMENTS
# ==============================================================
# If the original function takes arguments, the WRAPPER must accept
# them too and pass them on to the original function.

def greeting(func):
    def wrapper(name):
        result = func(name)             # pass the argument along
        return 'HELLO ' + str(result)
    return wrapper

@greeting
def their_func(name):
    return name

print(their_func('Uzair'))      # HELLO Uzair


# --- One decorator for ANY function: use *args and **kwargs ---
# (We learned *args and **kwargs in Class 10.)
# *args    -> collects any number of normal arguments
# **kwargs -> collects any number of keyword arguments (name=value)

def show_details(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, 'with', args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@show_details
def add(a, b):
    return a + b

@show_details
def full_name(first, last='Khan'):
    return first + ' ' + last

print(add(5, 7))
print(full_name('Ayan', last='Ali'))
print()


# --- Real-life use case: checking before running ---
# Decorators are used a lot in real projects (web apps, AI agents)
# to check things like "is the user logged in?" before running code.

def only_positive(func):
    def wrapper(number):
        if number < 0:
            return 'Error: number must be positive!'
        return func(number)
    return wrapper

@only_positive
def square_root(number):
    return number ** 0.5

print(square_root(49))      # 7.0
print(square_root(-4))      # Error: number must be positive!
print()


# ==============================================================
# 4. LAMBDA FUNCTIONS
# ==============================================================
# A LAMBDA is a small function written in ONE line, without a name.
#
#   SYNTAX:   lambda arguments : expression
#
#   - It can take MANY arguments
#   - But it can only have ONE expression
#   - The result of that expression is returned automatically
#     (no 'return' keyword needed)
#
# These two are the SAME:
#
#   def add_ten(a):               add_ten = lambda a: a + 10
#       return a + 10

add_ten = lambda a: a + 10
print(add_ten(20))                  # 30

# Multiple arguments
add_two = lambda a, b: a + b
print(add_two(44, 51))              # 95

say_hi = lambda a, b: 'HELLO ' + a + ' and ' + b
print(say_hi('Ayan', 'Ibrahim'))    # HELLO Ayan and Ibrahim

# Lambda with if-else (short-hand if-else from Class 8)
even_or_odd = lambda n: 'Even' if n % 2 == 0 else 'Odd'
print(even_or_odd(7))               # Odd
print(even_or_odd(10))              # Even
print()


# ==============================================================
# 5. LAMBDA WITH sorted(), map() AND filter()
# ==============================================================
# Lambdas are most useful when a function needs ANOTHER small
# function for a very short time.

students = [('Ali', 72), ('Sara', 95), ('Bilal', 60), ('Hina', 88)]

# sorted(..., key=...) -> sort by a rule we choose
# Here: sort by marks (index 1 of each tuple)
by_marks = sorted(students, key=lambda s: s[1])
print('Sorted by marks:', by_marks)

# Highest marks first
print('Toppers first :', sorted(students, key=lambda s: s[1], reverse=True))

# map(function, list) -> apply the function to EVERY item
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, numbers))
print('Squares:', squares)              # [1, 4, 9, 16, 25]

# filter(function, list) -> keep only the items where the function is True
evens = list(filter(lambda n: n % 2 == 0, numbers))
print('Evens  :', evens)                # [2, 4]
print()


# ==============================================================
# 6. A FUNCTION THAT RETURNS A FUNCTION
# ==============================================================
# The outer function "remembers" the value of num and builds
# a new function using it. This is like a function FACTORY.

def make_adder(num):
    return lambda a: a + num

add_20 = make_adder(20)     # a function that adds 20
add_100 = make_adder(100)   # a function that adds 100

print(type(add_20))         # <class 'function'>
print(add_20(40))           # 60
print(add_100(40))          # 140


def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))     # 10 15
print()


# ==============================================================
# 7. RECURSION
# ==============================================================
# RECURSION = a function that CALLS ITSELF.
#
# Every recursive function needs TWO parts:
#   1. BASE CASE      -> when to STOP (otherwise it runs forever!)
#   2. RECURSIVE CASE -> call itself with a SMALLER problem
#
# Like Russian nesting dolls: open a doll, find a smaller doll
# inside, keep going until you reach the smallest one (base case).

def countdown(n):
    if n <= 0:                  # BASE CASE
        print('DONE!')
    else:                       # RECURSIVE CASE
        print(n)
        countdown(n - 1)        # call itself with a smaller number

countdown(5)
print()


# --- Factorial ---
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# Notice:  5! = 5 x 4!
#          4! = 4 x 3!   ... and so on, until 1! = 1

def factorial(n):
    if n == 0 or n == 1:            # BASE CASE
        return 1
    else:                           # RECURSIVE CASE
        return n * factorial(n - 1)

print('5! =', factorial(5))         # 120

# How factorial(4) is solved, step by step:
#
#   factorial(4) = 4 * factorial(3)
#                      factorial(3) = 3 * factorial(2)
#                                         factorial(2) = 2 * factorial(1)
#                                                            factorial(1) = 1   <- BASE CASE
#                                         factorial(2) = 2 * 1 = 2
#                      factorial(3) = 3 * 2 = 6
#   factorial(4) = 4 * 6 = 24


# --- Sum of numbers from 1 to n ---
def sum_to(n):
    if n == 0:                      # BASE CASE
        return 0
    return n + sum_to(n - 1)        # RECURSIVE CASE

print('1 + 2 + ... + 10 =', sum_to(10))     # 55


# --- Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13 ... ---
# Each number = the sum of the two numbers before it
def fibonacci(n):
    if n <= 1:                      # BASE CASE
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=' ')
print('\n')

# WARNING: If you forget the base case, Python keeps calling the
# function until it gives a RecursionError (about 1000 calls deep).


# ==============================================================
# 8. PRACTICE EXAMPLES
# ==============================================================

# --- Reverse a string using recursion ---
def reverse(text):
    if text == '':                          # BASE CASE: empty string
        return ''
    return reverse(text[1:]) + text[0]      # rest reversed + first letter

print(reverse('Python'))            # nohtyP

# --- Decorator that makes any result uppercase ---
def shout(func):
    def wrapper(*args):
        return str(func(*args)).upper() + '!!!'
    return wrapper

@shout
def welcome(name):
    return 'welcome to agentic ai, ' + name

print(welcome('students'))

# --- Lambda to calculate the price after discount ---
discount = lambda price, percent: price - price * percent / 100
print('Price after 20% off:', discount(2500, 20))
