"""
================================================================
 Module 1 - Python Basics | Class 3: String Operations & Slicing
================================================================

Topics covered in this class:
    1. Multi-line strings    - using triple quotes
    2. String methods        - upper(), lower(), title()
    3. Checking methods      - islower(), isnumeric(), isalpha()
    4. Indexing              - getting ONE character: course[0]
    5. Slicing               - getting a PART: course[start:end:step]
    6. Common mistakes       - errors to watch out for
    7. print() tips          - the end parameter and '\\n'
"""

# import os

course = 'Agentic AI'
print(course)


# ==============================================================
# 1. MULTI-LINE STRINGS
# ==============================================================
# Triple quotes (''' or """) let a string span many lines.
# When stored in a variable, it is a real string (not a comment).

description = '''
I'm Muhammad Uzair Khan, a Data Engineer, AI Engineer, and Data Scientist with a
passion for cloud computing, scalable data solutions, and
AI-driven applications. I specialize in building
high-performance data pipelines, real-time streaming solutions,
and AI-powered systems that drive efficiency and innovation. 🚀
'''
print(description)


# ==============================================================
# 2. STRING METHODS (changing the case)
# ==============================================================
# A method is a function that belongs to a value: value.method()
# These return a NEW string; the original stays the same.

print(course.upper())    # AGENTIC AI
print(course.lower())    # agentic ai
print(course.title())    # Agentic Ai  (first letter of each word capital)

# ⚠️ Don't forget the brackets ()!
print(course.title)      # Prints <built-in method title ...> instead of the text


# ==============================================================
# 3. CHECKING METHODS (return True or False)
# ==============================================================
print(course.islower())      # False -> are ALL letters lowercase?
print(course.isnumeric())    # False -> does it contain ONLY numbers?
print(course.isalpha())      # False -> ONLY letters? (the space is not a letter!)
print('UZAIR'.isalpha())     # True

var = '123'
print(var.isnumeric())       # True

# ⚠️ String methods only work on strings:
# var = 123
# print(var.isnumeric())     # AttributeError: 'int' object has no attribute 'isnumeric'

# os.system('cls')     # Windows
# os.system('clear')   # macOS / Linux


# ==============================================================
# 4. INDEXING - getting ONE character
# ==============================================================
# Every character has a position number (index), starting from 0.
# Negative indexes count from the end, starting from -1.
#
#     A    g    e    n    t    i    c         A    I
#     0    1    2    3    4    5    6    7    8    9
#   -10   -9   -8   -7   -6   -5   -4   -3   -2   -1
#
# (index 7 is the SPACE)

print(course[0])     # A   -> first character
print(course[9])     # I   -> last character
print(course[-1])    # I   -> last character (counting from the end)
print(course[7])     # ' ' -> the space

# ⚠️ Only square brackets [ ] are used for indexing:
# print(course(7))   # TypeError: 'str' object is not callable

# ⚠️ An index that doesn't exist gives an error:
# print(course[10])  # IndexError: string index out of range


# ==============================================================
# 5. SLICING - getting a PART of a string
# ==============================================================
# Syntax:   string[start : end : step]
#   start -> INCLUDED  (where to begin)
#   end   -> EXCLUDED  (stops just BEFORE this index)
#   step  -> how many characters to jump (default is 1)

# --- Start and end ---
print(course[0:7])     # Agentic
print(course[0:8])     # 'Agentic ' (includes the space)
print(course[0:9])     # Agentic A
print(course[-6:-3])   # tic

print(course[-3:-6])   # '' -> empty! start must come BEFORE end

# --- From the start up to an index (leave start empty) ---
print(course[:6])      # Agenti
print(course[:-5])     # Agent

# --- From an index to the end (leave end empty) ---
print(course[7:])      # ' AI'
print(course[-3:])     # ' AI'

# --- Everything ---
print(course[::])      # Agentic AI
print(course[:])       # Agentic AI

# --- Step (interval) ---
print(course[::2])     # AetcA  -> every 2nd character
print(course[::3])     # AncI   -> every 3rd character
print(course[2:-3:3])  # ei     -> from index 2, before -3, every 3rd
print(course[::-1])    # IA citnegA -> a negative step REVERSES the string


# ==============================================================
# 6. COMMON MISTAKES
# ==============================================================
# ❌ Logical error: this prints 'A' and the list [8], not two characters
print(course[0], [8])
# ✅ Correct:
print(course[0], course[8])

# ❌ You cannot take two slices in one bracket:
# print(course[0:3, 7:9])   # TypeError
# ✅ Take them separately, then print or join them:
print(course[:3], course[7:])      # Age  AI  (comma adds a space)
print(course[:3] + course[7:])     # Age AI   (+ joins them directly)


# ==============================================================
# 7. print() TIPS - '\n' and end
# ==============================================================
# '\n' is a "new line" character.
# By default print() ends with '\n'. The end parameter changes that.

print('Line 1', end=' | ')    # stays on the same line
print('Line 2')               # Line 1 | Line 2
print(course, end='\n\n')     # adds an extra empty line after

print('CLASS END')
