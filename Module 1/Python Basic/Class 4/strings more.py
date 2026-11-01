"""
================================================================
 Module 1 - Python Basics | Class 4 (Part 1): More on Strings
================================================================

Topics covered in this file:
    1. String formatting   - 3 ways to mix text and variables
    2. f-strings           - the modern, recommended way
    3. Escape sequences    - \\'  \\"  \\\\  \\n  \\t  \\b
    4. String methods      - find(), rfind(), split(), strip()

Run order for Class 4:
    1. strings more.py   <-- you are here
    2. lists.py
"""

name = 'Irtiza'   # str
age = 22          # int


# ==============================================================
# 1. STRING FORMATTING - mixing text with variables
# ==============================================================
# Hard-coded text (doesn't change if the variables change):
print('My name is Irtiza and my age is 22')

# Way 1: Concatenation with +
# Every piece must be a string, so we convert age with str().
print('My name is ' + name + ' and my age is ' + str(age))

# Way 2: Commas inside print()
# Works with any type and adds spaces automatically.
print('My name is', name, 'and my age is', age)


# ==============================================================
# 2. f-STRINGS (formatted strings) - RECOMMENDED
# ==============================================================
# Put an f before the quotes, then write variables inside { }.
# No str() needed and no worrying about spaces!

print(f'My name is {name} and my age is {age}')

# You can even do calculations inside { }:
print(f'Next year I will be {age + 1}')


# ==============================================================
# 3. ESCAPE SEQUENCES - special characters using a backslash \
# ==============================================================
# Problem: using the same quote inside a string breaks it.
# print('My name is 'Irtiza' and my age is 22')   # SyntaxError

# Fix 1: use the OTHER type of quotes outside
print("My name is 'Irtiza' and my age is 22")
print('My name is "Irtiza" and my age is 22')

# Fix 2: escape the quote with a backslash  ->  \'  or  \"
print('My name is \'Irtiza\' and my age is 22')

# A forward slash / is a normal character, no escaping needed:
print('My name is /Irtiza/ and my age is 22')

# \\  -> prints ONE backslash
print('My name is \\Irtiza\\ and my age is 22')

# \n  -> new line
print('\nMy name is Irtiza and\nmy age is 22')

# \t  -> tab (a big space)
print('My name is Irtiza\tmy age is 22')

# \b  -> backspace (deletes the character before it)
print('My name is Irtiza a\bnd my age is 22')   # 'a' is removed -> "nd"
# Note: \b may look different in some terminals (e.g. VS Code output panel).

# Summary:
#   \'  single quote      \"  double quote      \\  backslash
#   \n  new line          \t  tab               \b  backspace


# ==============================================================
# 4. STRING METHODS - find(), rfind(), split(), strip()
# ==============================================================
txt = 'My name is Irtiza and my age is 22'

# --- find() -> returns the STARTING index of the text ---
print(txt.find('and'))     # 18
print(txt[18:])            # and my age is 22

# find() is case-sensitive: 'My' and 'my' are different
print(txt.find('My'))      # 0
print(txt.find('my'))      # 22

# If the text is NOT found, find() returns -1
print(txt.find('Ali'))     # -1

# --- rfind() -> searches from the END (right side) ---
print(txt.find('is'))      # 8   -> first 'is'
print(txt.rfind('is'))     # 29  -> last 'is'

# --- split() -> breaks a string into a LIST of pieces ---
print(txt.split(' '))      # split on every space
print(txt.split('and'))    # ['My name is Irtiza ', ' my age is 22']

# --- strip() -> removes extra spaces from the START and END ---
part = txt.split('and')[1]
print(f'[{part}]')               # [ my age is 22]   (space at the start)
print(f'[{part.strip()}]')       # [my age is 22]

# Tip: to clear the terminal screen from Python:
# import os
# os.system('cls')     # Windows
# os.system('clear')   # macOS / Linux
