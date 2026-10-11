"""
================================================================
 Module 1 - Python Basics | Class 2 (Part 1): Variables & Types
================================================================

Topics covered in this file:
    1. Case sensitivity      - Email and email are different variables
    2. String concatenation  - joining strings with +
    3. Checking types        - using the type() function
    4. Mixing int and float  - what happens when we add them

Run order for Class 2:
    1. variables and types.py   <-- you are here
    2. data types.py
    3. type casting.py
"""

print('This is Class 2')


# ==============================================================
# 1. CASE SENSITIVITY
# ==============================================================
# Python treats uppercase and lowercase letters as DIFFERENT.
# So 'Email' and 'email' are two separate variables.

Email = 'huzaifa'
print(Email)

email = 'uzair'
print(email)


# ==============================================================
# 2. STRING CONCATENATION
# ==============================================================
# Concatenation means joining strings together using the + sign.
# Note: + does NOT add a space. You must add it yourself.

print('Example of Concatenation:', Email + email)   # huzaifauzair
print(Email + ' ' + email)                          # huzaifa uzair

# Quotes make the difference between TEXT and a VARIABLE:
print("email" + Email)   # "email" is plain text, Email is a variable


# ==============================================================
# 3. CHECKING TYPES WITH type()
# ==============================================================
# type() tells us what kind of value a variable is holding.
# Tip: a comma ( , ) inside print() automatically adds a single space.

x = 10        # int   (whole number)
print(x)
print('Value X is:', type(x))

y = '20'      # str   (text - because it is inside quotes!)
print('Value Y is:', type(y))

z = 5.5       # float (decimal number)
a = 'Value Z is:'
print(a, type(z))


# ==============================================================
# 4. MIXING int AND float
# ==============================================================
# When you add an int and a float, Python gives back a float.

ans = x + z        # 10 + 5.5
print(ans)         # 15.5
print(type(ans))   # <class 'float'>

# But you CANNOT add a number and a string:
# print(x + y)     # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# We will fix this using type casting in "type casting.py".
