"""
================================================================
 Module 1 - Python Basics | Class 5 (Part 1): Lists (Continued)
================================================================

Lists are ORDERED and MUTABLE.

Topics covered in this file:
    1. Recap                - append(), insert(), pop(), remove()
    2. extend()             - add one list into another
    3. reverse()            - flip the order
    4. clear()              - empty the whole list
    5. sort()               - A-Z and Z-A
    6. Copying a list       - why  b = a  is NOT a copy
    7. len()                - count the items

Run order for Class 5:
    1. lists.py    <-- you are here
    2. tuples.py
"""


# ==============================================================
# 1. RECAP
# ==============================================================
fruits = ['apple', 'mango']
fruits.append('orange')       # ['apple', 'mango', 'orange']
fruits[1] = 'cherry'          # ['apple', 'cherry', 'orange']
fruits.insert(2, 'grapes')    # ['apple', 'cherry', 'grapes', 'orange']
fruits.pop()                  # removes the LAST item  -> 'orange'
fruits.pop(1)                 # removes INDEX 1        -> 'cherry'
fruits.remove('grapes')       # removes by exact VALUE
print(fruits)                 # ['apple']


# ==============================================================
# 2. extend() - add all items of another list
# ==============================================================
fruits_2 = ['watermelon', 'guava', 'kiwi']
fruits.extend(fruits_2)
print(fruits)    # ['apple', 'watermelon', 'guava', 'kiwi']

# append() vs extend():
#   fruits.append(['a', 'b'])  -> adds the whole list as ONE item
#   fruits.extend(['a', 'b'])  -> adds 'a' and 'b' as separate items


# ==============================================================
# 3. reverse() - flip the order
# ==============================================================
fruits.reverse()
print(fruits)    # ['kiwi', 'guava', 'watermelon', 'apple']


# ==============================================================
# 4. clear() - remove ALL items
# ==============================================================
# Uncomment to try (it would empty our list for the rest of the file):
# fruits.clear()
# print(fruits)  # []


# ==============================================================
# 5. sort() - arrange items in order
# ==============================================================
fruits.sort()                # A -> Z  (numbers: small -> big)
print(fruits)
fruits.sort(reverse=True)    # Z -> A  (numbers: big -> small)
print(fruits)


# ==============================================================
# 6. COPYING A LIST
# ==============================================================
# --- Assignment ( = ) is NOT a copy ---
# b = a just gives the SAME list a second name.
# Changing one name changes the other too!
fruits_copy = fruits
print(fruits_copy.pop())     # removes from BOTH (same list)
print(fruits_copy)
print(fruits)                # also changed!

# --- copy() makes a real, separate copy ---
fruits_copy = fruits.copy()
fruits_copy.append('banana')
print(fruits)                # unchanged
print(fruits_copy)           # has 'banana'

# Note: copy() is called a SHALLOW copy. It's perfect for simple lists.
# For lists that contain other lists, use a DEEP copy:
#   import copy
#   new_list = copy.deepcopy(old_list)


# ==============================================================
# 7. len() - number of items
# ==============================================================
print(len(fruits))
print(len(fruits_copy))
print(type(len(fruits)))     # <class 'int'>
