"""
================================================================
 Module 1 - Python Basics | Class 4 (Part 2): Lists (Introduction)
================================================================

A LIST stores multiple items in a single variable.
    fruits = ['apple', 'mango', 'banana']

Lists are:
    - ORDERED   -> every item has a position (index)
    - MUTABLE   -> you can add, change and remove items
    - Allow DUPLICATES and can hold ANY data type

Topics covered in this file:
    1. Turning a string into a list   - replace() + split()
    2. Indexing & slicing             - same as strings!
    3. Adding items                   - append(), insert()
    4. Changing an item               - list[index] = value
    5. Removing items                 - pop(), remove()
"""


# ==============================================================
# 1. TURNING A STRING INTO A LIST
# ==============================================================
fruits = 'apple, mango, banana, peach, orange, grapes, cherry, kiwi, pineapple, pear'
print(type(fruits))     # <class 'str'> -> this is ONE long string

# replace(old, new) -> replaces text. Here we remove all spaces.
# split(',')        -> cuts the string at every comma into a list.
var = fruits.replace(' ', '').split(',')
print(var)
print(type(var))        # <class 'list'>

# You can also create a list directly with square brackets [ ]:
numbers = [10, 20, 30]
mixed = ['Ali', 22, 5.5, True]   # different data types are allowed
print(numbers, mixed)


# ==============================================================
# 2. INDEXING & SLICING (works exactly like strings)
# ==============================================================
# ['apple', 'mango', 'banana', 'peach', 'orange', ...]
#     0        1        2         3        4

print(var[2])      # banana        -> one item
print(var[-2])     # pineapple     -> second from the end
print(var[:2])     # ['apple', 'mango']   -> first two items
print(var[4:])     # from index 4 to the end


# ==============================================================
# 3. ADDING ITEMS
# ==============================================================
# append(value) -> adds ONE item at the END
var.append('strawberry')
print(var)

# insert(index, value) -> adds an item at a specific position
var.insert(0, 'avocado')    # add at the start
print(var)


# ==============================================================
# 4. CHANGING AN ITEM
# ==============================================================
# Use the index to replace the value at that position.
var[7] = 'berry'            # replaces 'cherry' with 'berry'
print(var)


# ==============================================================
# 5. REMOVING ITEMS
# ==============================================================
# pop() -> removes the LAST item and RETURNS it
print(var.pop())            # strawberry
print(var)

# pop(index) -> removes the item at that index and returns it
print(var.pop(3))           # banana
print(var)

# remove(value) -> removes the first matching VALUE (case-sensitive)
var.remove('apple')
print(var)
# var.remove('Apple')       # ValueError: 'Apple' is not in list

# Summary:
#   pop()        -> remove by INDEX  (default: last item)
#   remove()     -> remove by VALUE
