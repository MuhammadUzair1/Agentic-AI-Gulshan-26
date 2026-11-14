"""
================================================================
 Module 1 - Python Basics | Class 9 (Part 1): While Loop
================================================================

What is a LOOP?
    A loop REPEATS a block of code again and again,
    so you don't have to write the same line 100 times.

Python has 2 types of loops:
    - while loop  -> repeats WHILE a condition is True   (you are here)
    - for loop    -> repeats for EACH item in a sequence (next file)

Topics covered in this file:
    1. Basic while loop
    2. How it works (step-by-step trace)
    3. Real examples: countdown, sum of numbers, table
    4. break     - STOP the loop early
    5. continue  - SKIP the rest of this round, go to the next one
    6. else      - runs once when the loop finishes normally
    7. ⚠️ Infinite loops (and how to avoid them)

Run order for Class 9:
    1. while loop.py   <-- you are here
    2. for loop.py
"""


# ==============================================================
# 1. BASIC WHILE LOOP
# ==============================================================
# Syntax:
#     while condition:
#         # loop body (indented) - repeats while condition is True
#
# Every while loop needs 3 things:
#     1. START    -> a starting value          num = 1
#     2. CHECK    -> a condition               num < 10
#     3. CHANGE   -> update the value          num = num + 1

num = 1                  # 1. START
while num < 10:          # 2. CHECK
    print(num)           #    loop body
    num = num + 1        # 3. CHANGE (can also be written as: num += 1)

print('END\n')


# ==============================================================
# 2. HOW IT WORKS - STEP BY STEP
# ==============================================================
#   | Round | num | num < 4 ? | What happens        |
#   |-------|-----|-----------|---------------------|
#   |   1   |  1  |   True    | print 1, num -> 2   |
#   |   2   |  2  |   True    | print 2, num -> 3   |
#   |   3   |  3  |   True    | print 3, num -> 4   |
#   |   -   |  4  |   False   | loop STOPS          |

num = 1
while num < 4:
    print('Round', num)
    num += 1

print('END\n')


# ==============================================================
# 3. REAL EXAMPLES
# ==============================================================
# --- Countdown 🚀 ---
count = 5
while count > 0:
    print(count)
    count -= 1           # same as: count = count - 1
print('Launch! 🚀\n')

# --- Sum of numbers from 1 to 10 ---
num = 1
total = 0
while num <= 10:
    total = total + num  # add the current number to the total
    num += 1
print('Sum of 1 to 10 =', total, '\n')   # 55

# --- Multiplication table of 2 ---
i = 1
while i <= 10:
    print(f'2 x {i} = {2 * i}')
    i += 1
print()


# ==============================================================
# 4. break - STOP THE LOOP EARLY
# ==============================================================
# When Python reaches 'break', it jumps OUT of the loop immediately.

num = 1
while num < 10:
    print(num)
    if num == 5:
        print('BREAK')
        break            # exit the loop - 6, 7, 8, 9 are never printed
    num += 1

print('END\n')

# Real example: only 3 password attempts allowed
correct_password = 'agentic123'
attempts = ['hello', 'agentic123', 'abc']   # pretend these were typed by the user
# (In a real program you would use: guess = input('Password: '))

tries = 0
while tries < 3:
    guess = attempts[tries]
    tries += 1
    print(f'Attempt {tries}: {guess}')
    if guess == correct_password:
        print('Login successful 🔓')
        break
print('END\n')


# ==============================================================
# 5. continue - SKIP THIS ROUND
# ==============================================================
# When Python reaches 'continue', it SKIPS the rest of the loop body
# and jumps back to the condition for the next round.
# Here we skip printing 5:

num = 0
while num < 9:
    num += 1             # ⚠️ change the value BEFORE continue (see section 7)
    if num == 5:
        continue         # skip the print below when num is 5
    print(num)           # prints 1 2 3 4 6 7 8 9

print('END\n')

# break vs continue:
#   break     -> leaves the loop completely
#   continue  -> skips only the current round, the loop keeps going


# ==============================================================
# 6. else WITH A LOOP
# ==============================================================
# The else block runs ONCE when the loop condition becomes False.
# It does NOT run if the loop was stopped by 'break'.

num = 1
while num < 4:
    print(num)
    num += 1
else:
    print("LOOP ENDED :')")   # runs - the loop finished normally

num = 1
while num < 4:
    if num == 2:
        break
    print(num)
    num += 1
else:
    print('This will NOT print, because we used break')

print('END\n')


# ==============================================================
# 7. ⚠️ INFINITE LOOPS
# ==============================================================
# If the condition NEVER becomes False, the loop runs FOREVER.
#
#   num = 1
#   while num < 10:
#       print(num)       # forgot num += 1  -> prints 1 forever!
#
# Common causes:
#   - forgetting to update the variable
#   - putting 'continue' BEFORE the update (the update gets skipped)
#
# 🛑 Stuck in an infinite loop? Press  Ctrl + C  in the terminal to stop it.
