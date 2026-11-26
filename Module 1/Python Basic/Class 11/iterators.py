"""
================================================================
 Module 1 - Python Basics | Class 11 (Part 2): Iterators
================================================================

An ITERABLE is anything you can loop over:
    list, tuple, string, set, dictionary, range ...

An ITERATOR is an object that gives you the items of an iterable
ONE AT A TIME, and remembers where it stopped.

Think of a PEZ / tissue box:
    - The box (iterable) holds all the items.
    - Each time you pull (next), you get the NEXT item.
    - When the box is empty, you can't pull any more.

Two built-in functions:
    iter(iterable) -> creates an iterator from an iterable
    next(iterator) -> gives the next item

Topics covered in this file:
    1. iter() and next()
    2. StopIteration - when the items run out
    3. Iterators on strings, lists and dictionaries
    4. How a for loop really works
    5. Generators - an easy way to make your own iterator (yield)
    6. Practice examples
"""


# ==============================================================
# 1. iter() AND next()
# ==============================================================
my_tuple = (30, 50, 70, 90)
my_it = iter(my_tuple)          # create an iterator

print(next(my_it))      # 30
print(next(my_it))      # 50
print(next(my_it))      # 70
print(next(my_it))      # 90
print()

# The iterator REMEMBERS where it stopped. We can take a few items,
# do something else, and continue later from the same place.
colours = iter(['red', 'green', 'blue', 'yellow'])
print('First :', next(colours))
print('Second:', next(colours))
print('... doing some other work ...')
print('Third :', next(colours))      # continues from where it stopped
print()


# ==============================================================
# 2. StopIteration - WHEN THE ITEMS RUN OUT
# ==============================================================
# If we call next() after the last item, Python raises an error
# called StopIteration. (We will learn try / except in Class 12.)

small = iter([1, 2])
print(next(small))      # 1
print(next(small))      # 2
# print(next(small))    # ERROR: StopIteration  (uncomment to see)

# next() can take a DEFAULT value to return instead of an error
print(next(small, 'No more items!'))
print()


# ==============================================================
# 3. ITERATORS ON STRINGS, LISTS AND DICTIONARIES
# ==============================================================
# A string gives one CHARACTER at a time
letters = iter('AI')
print(next(letters))    # A
print(next(letters))    # I

# A dictionary gives one KEY at a time
student = {'name': 'Sara', 'age': 20, 'city': 'Karachi'}
keys = iter(student)
print(next(keys))       # name
print(next(keys))       # age

# range() is also an iterable
nums = iter(range(100, 103))
print(next(nums), next(nums), next(nums))   # 100 101 102
print()


# ==============================================================
# 4. HOW A FOR LOOP REALLY WORKS
# ==============================================================
# When you write:
#
#     for fruit in fruits:
#         print(fruit)
#
# Python secretly does this:
#     1. it = iter(fruits)
#     2. fruit = next(it)  ... run the loop body ... repeat
#     3. when StopIteration happens -> the loop ends quietly

fruits = ['apple', 'mango', 'banana']

# Normal for loop
for fruit in fruits:
    print(fruit)
print()

# The same thing done "by hand" with a while loop
it = iter(fruits)
while True:
    fruit = next(it, None)      # None when the list is finished
    if fruit is None:
        break
    print(fruit)
print()


# ==============================================================
# 5. GENERATORS - MAKE YOUR OWN ITERATOR WITH yield
# ==============================================================
# A GENERATOR is a function that uses 'yield' instead of 'return'.
#
#   return -> gives ONE value and the function is FINISHED
#   yield  -> gives a value, PAUSES, and continues from the same
#             line the next time you ask with next()

def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number            # give a value and pause here
        number += 1             # continue from here next time

counter = count_up_to(3)
print(next(counter))    # 1
print(next(counter))    # 2
print(next(counter))    # 3

# Generators work in for loops too
for n in count_up_to(5):
    print(n, end=' ')
print('\n')

# Why are generators useful?
# They create values ONLY when needed, so they use very little memory.
# A list of 1 million numbers takes a lot of memory;
# a generator of 1 million numbers takes almost none.


# ==============================================================
# 6. PRACTICE EXAMPLES
# ==============================================================

# --- Queue at a bank counter: serve customers one by one ---
customers = iter(['Ali', 'Sara', 'Bilal'])
print('Now serving:', next(customers))
print('Now serving:', next(customers))
print('Now serving:', next(customers))
print('Now serving:', next(customers, 'Nobody - queue is empty'))
print()

# --- Generator for even numbers ---
def even_numbers(limit):
    for n in range(2, limit + 1, 2):
        yield n

print('Even numbers up to 12:', list(even_numbers(12)))

# --- Generator for a multiplication table ---
def table(n):
    for i in range(1, 6):
        yield f'{n} x {i} = {n * i}'

for line in table(7):
    print(line)
