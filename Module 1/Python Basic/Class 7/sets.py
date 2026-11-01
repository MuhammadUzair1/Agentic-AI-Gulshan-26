"""
================================================================
 Module 1 - Python Basics | Class 7 (Part 2): Sets
================================================================

A SET stores multiple UNIQUE items.
    this_set = {'apple', 'mango', 'orange'}     <- curly brackets { }

Sets are:
    - UNORDERED     -> no fixed order, so NO indexing:  this_set[0] -> TypeError
    - NO DUPLICATES -> each value appears only once
    - MUTABLE       -> you CAN add and remove items
                       (but the items themselves must be unchangeable
                        types like str, int, tuple - not lists)

Topics covered in this file:
    1. Creating a set
    2. Removing duplicates from a list
    3. len()
    4. add()
    5. pop() and remove()

Run order for Class 7:
    1. dictionary recap.ipynb
    2. sets.py    <-- you are here
"""


# ==============================================================
# 1. CREATING A SET
# ==============================================================
this_set = {'apple', 'mango', 'orange'}
print(type(this_set))   # <class 'set'>
print(this_set)         # the order may be different every time you run!

# ⚠️ {} creates an EMPTY DICTIONARY, not a set. Use set() instead:
empty = set()
print(type(empty))      # <class 'set'>


# ==============================================================
# 2. REMOVING DUPLICATES FROM A LIST (most common use!)
# ==============================================================
dup_list = [1, 2, 3, 1, 5, 6, 3]
print(dup_list)

myset = set(dup_list)   # list -> set   (duplicates removed)
mylist = list(myset)    # set  -> list  (back to a list)
print(mylist)           # [1, 2, 3, 5, 6]


# ==============================================================
# 3. len() - number of items
# ==============================================================
print(len(this_set))    # 3


# ==============================================================
# 4. add() - add ONE item
# ==============================================================
this_set.add('grape')
print(this_set)

this_set.add('mango')   # already exists -> nothing changes
print(this_set)


# ==============================================================
# 5. REMOVING ITEMS
# ==============================================================
# pop() -> removes and returns a RANDOM item (sets have no "last" item)
print(this_set.pop())
print(this_set)

# remove(value) -> removes that exact value
this_set.add('apple')   # make sure 'apple' is there (pop may have removed it)
this_set.remove('apple')
print(this_set)
# this_set.remove('banana')   # KeyError: 'banana' is not in the set

# Summary - List vs Tuple vs Set vs Dictionary:
#   | Type  | Brackets      | Ordered | Changeable | Duplicates  |
#   |-------|---------------|---------|------------|-------------|
#   | list  | [1, 2]        | Yes     | Yes        | Yes         |
#   | tuple | (1, 2)        | Yes     | No         | Yes         |
#   | set   | {1, 2}        | No      | Yes        | No          |
#   | dict  | {'a': 1}      | Yes     | Yes        | No (keys)   |
