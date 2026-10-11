"""
================================================================
 Module 1 - Python Basics | Class 2 (Part 2): Data Types
================================================================

Topics covered in this file:
    Numbers:
        1. int      - whole numbers           e.g. 10, -5, 0
        2. float    - decimal numbers         e.g. 2.5, -0.75
        3. complex  - numbers with j          e.g. 4j, 2 + 3j
    Others:
        4. str      - text inside quotes      e.g. 'uzair'
        5. bool     - True or False
        6. NoneType - None (means "no value")

Quick summary:
    | Type     | Example     | Used for                     |
    |----------|-------------|------------------------------|
    | int      | 25          | age, count, marks            |
    | float    | 99.5        | price, percentage, weight    |
    | complex  | 4j          | advanced maths / engineering |
    | str      | 'Agentic'   | names, emails, messages      |
    | bool     | True        | yes/no, on/off, pass/fail    |
    | NoneType | None        | empty / no value yet         |
"""


# ==============================================================
# 1. INTEGER (int) - whole numbers, positive, negative or zero
# ==============================================================
x = 10
print(x, type(x))

t = 2153201321430       # big numbers are fine
u = -14651635468        # negative numbers
v = 0                   # zero
print(t, u, v)

# Note: a whole number CANNOT start with 0 in Python.
# t = 02153201321430    # SyntaxError: leading zeros are not allowed
# Tip: for phone numbers / CNIC, use a string instead: '03001234567'


# ==============================================================
# 2. FLOAT - numbers with a decimal point
# ==============================================================
y = 2.5
print(y, type(y))

price = 10.0            # still a float because of the .0
print(price, type(price))


# ==============================================================
# 3. COMPLEX - numbers with a "j" part (used in advanced maths)
# ==============================================================
c = 4j
print(c, type(c))


# ==============================================================
# 4. STRING (str) - text inside quotes
# ==============================================================
z = 'uzair'
print(z, type(z))

number_as_text = '100'  # inside quotes, so it is TEXT, not a number
print(number_as_text, type(number_as_text))


# ==============================================================
# 5. BOOLEAN (bool) - only two values: True or False
# ==============================================================
# Note: True and False must start with a CAPITAL letter.
b = True
a = False
print(type(a), type(b))


# ==============================================================
# 6. NONE (NoneType) - means "nothing" / "no value yet"
# ==============================================================
d = None
print(d, type(d))
