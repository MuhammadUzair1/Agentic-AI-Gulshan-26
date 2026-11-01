"""
================================================================
 Module 1 - Python Basics | Class 5 (Part 2): Tuples
================================================================

A TUPLE is like a list, but it CANNOT be changed after creation.
    mytuple = (12, 354, 'abc')      <- round brackets ( )

Tuples are:
    - ORDERED     -> indexing and slicing work like lists
    - IMMUTABLE   -> you can't add, change or remove items
    - Allow DUPLICATES

Use a tuple for data that should never change,
e.g. days of the week, GPS coordinates, RGB colours.

Topics covered in this file:
    1. Creating a tuple
    2. Indexing & slicing
    3. Immutability (can't change items)
    4. Duplicates and len()
    5. "Adding" items (convert to list and back)
    6. Tuple unpacking (and the * operator)
"""


# ==============================================================
# 1. CREATING A TUPLE
# ==============================================================
mytuple = (12, 354, 6, 92, 'abc')
print(type(mytuple))    # <class 'tuple'>
print(mytuple)


# ==============================================================
# 2. INDEXING & SLICING (exactly the same as lists)
# ==============================================================
print(mytuple[0])       # 12
print(mytuple[0:2])     # (12, 354)
print(mytuple[-1])      # abc


# ==============================================================
# 3. TUPLES ARE IMMUTABLE
# ==============================================================
# You cannot change an item once the tuple is created:
# mytuple[0] = 1        # TypeError: 'tuple' object does not support item assignment


# ==============================================================
# 4. DUPLICATES AND len()
# ==============================================================
tuple2 = (1, 1, 2, 3)
print(tuple2)
print(len(tuple2))      # 4


# ==============================================================
# 5. "ADDING" ITEMS TO A TUPLE
# ==============================================================
# Trick: convert to a list -> change it -> convert back to a tuple.
mytuple = list(mytuple)
mytuple.append('xyz')
mytuple = tuple(mytuple)
print(mytuple)          # (12, 354, 6, 92, 'abc', 'xyz')


# ==============================================================
# 6. TUPLE UNPACKING
# ==============================================================
# Unpacking = putting each item into its own variable in one line.
# The number of variables must match the number of items.
print(tuple2)
(a, b, c, d) = tuple2
print(a, b, c, d)       # 1 1 2 3
print(type(a))          # <class 'int'>

# (a, b) = tuple2       # ValueError: too many values to unpack

# --- Using * to collect "the rest" into a list ---
fruits = ('apple', 'mango', 'grapes', 'kiwi', 'melon', 'orange')
(x, *y, z) = fruits
print(fruits)
print(x)                # apple                -> first item
print(y)                # ['mango', 'grapes', 'kiwi', 'melon']  -> everything in the middle
print(z)                # orange               -> last item
