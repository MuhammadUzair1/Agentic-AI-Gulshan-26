"""
================================================================
 Module 1 - Python Basics | Class 9 (Part 2): For Loop
================================================================

A FOR loop goes through items ONE BY ONE:
    "For EACH item in this collection, do something."

    for fruit in ['apple', 'mango', 'kiwi']:
        print(fruit)

while vs for:
    - while -> use when you DON'T know how many times to repeat
               (e.g. "keep asking until the password is correct")
    - for   -> use when you DO know (a list, a string, a range of numbers)

Topics covered in this file:
    1. range()                 - looping over numbers
    2. Looping over a list     - 3 ways
    3. Looping over a string
    4. break and continue in a for loop
    5. Looping over a dictionary
    6. Nested for loops        - a loop inside a loop
    7. Practice examples
"""


# ==============================================================
# 1. range() - LOOPING OVER NUMBERS
# ==============================================================
# range(start, end, step)
#   start -> where to begin      (INCLUDED, default = 0)
#   end   -> where to stop       (EXCLUDED - stops just before it)
#   step  -> how much to jump    (default = 1)
#
#   | Code              | Numbers produced     |
#   |-------------------|----------------------|
#   | range(5)          | 0 1 2 3 4            |
#   | range(1, 6)       | 1 2 3 4 5            |
#   | range(1, 10, 2)   | 1 3 5 7 9            |
#   | range(10, 1, -1)  | 10 9 8 7 6 5 4 3 2   |

for num in range(5):
    print(num)
print()

for num in range(1, 10, 1):
    print(num)
print()

# Counting backwards: use a NEGATIVE step
for num in range(10, 1, -1):
    print(num)
print()

# Tip: print(..., end=' ') keeps everything on one line
for num in range(1, 10, 2):
    print(num, end=' ')
print('\n')


# ==============================================================
# 2. LOOPING OVER A LIST
# ==============================================================
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# OPTION 1: directly over the items (simplest - use this most of the time)
for item in lst:
    print(item)
print()

# OPTION 2: over the indexes using range(len(...))
#   len(lst) = 8  ->  range(8) = 0, 1, 2 ... 7
for i in range(len(lst)):
    print(lst[i], 'is at index', i)
print()

# OPTION 3: enumerate() gives you BOTH the index and the item
for i, item in enumerate(lst):
    print(i, item)
print()


# ==============================================================
# 3. LOOPING OVER A STRING
# ==============================================================
# A string is a sequence of characters, so we can loop over it too.
name = 'UZAIR'
for letter in name:
    print(letter)
print()


# ==============================================================
# 4. break AND continue IN A FOR LOOP
# ==============================================================
# continue -> skip this letter and move to the next one
# break    -> stop the loop completely
#
# Rules for the loop below:
#   - skip spaces                       (continue)
#   - when we see a 'U', print 'UZAIR'  (continue)
#   - stop as soon as we see an 'I'     (break)
string = 'MUHAMMAD UZAIR'
for ch in string:
    if ch == ' ':
        continue
    elif ch.lower() == 'u':
        print('UZAIR')
        continue
    elif ch.lower() == 'i':
        break
    print(ch)
print()

# Trace:  M -> print | U -> 'UZAIR' | H, A, M, M, A, D -> print
#         ' ' -> skip | U -> 'UZAIR' | Z, A -> print | I -> STOP (R never printed)

# Real example: find the first even number in a list
numbers = [3, 7, 9, 12, 15, 18]
for n in numbers:
    if n % 2 == 0:
        print('First even number is', n)
        break
print()


# ==============================================================
# 5. LOOPING OVER A DICTIONARY
# ==============================================================
student = {'name': 'Ali', 'age': 20, 'city': 'Karachi'}

for key in student:                     # loops over the KEYS
    print(key)

for key, value in student.items():      # loops over key-value PAIRS
    print(f'{key}: {value}')
print()


# ==============================================================
# 6. NESTED FOR LOOPS - A LOOP INSIDE A LOOP
# ==============================================================
# For EVERY round of the outer loop, the inner loop runs COMPLETELY.

for i in range(1, 4):           # outer loop: 1, 2, 3
    for j in range(1, 3):       # inner loop: 1, 2  (runs fully each time)
        print(f'i = {i}, j = {j}')
print()

# Run the inner loop only when the outer item is 'f'
fruits = ['apple', 'guava', 'banana', 'grapes', 'kiwi']
for letter in lst:
    print(letter)
    if letter == 'f':
        for fruit in fruits:
            if fruit == 'grapes':
                continue        # skip grapes
            print('   ', fruit)
print()


# ==============================================================
# 7. PRACTICE EXAMPLES
# ==============================================================
# --- Sum of a list ---
marks = [80, 75, 90, 65]
total = 0
for m in marks:
    total += m
print('Total marks:', total)
print('Average:', total / len(marks))
print()

# --- Count the vowels in a word ---
word = 'Agentic AI'
vowels = 0
for ch in word.lower():
    if ch in 'aeiou':
        vowels += 1
print('Vowels in', word, '=', vowels)
print()

# --- Multiplication table of 5 ---
for i in range(1, 11):
    print(f'5 x {i} = {5 * i}')
print()

# --- Star pattern (nested loop) ---
for row in range(1, 6):
    for star in range(row):
        print('*', end='')
    print()        # move to the next line after each row

# Output:
# *
# **
# ***
# ****
# *****
