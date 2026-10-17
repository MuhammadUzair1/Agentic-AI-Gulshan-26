# LISTS
# Lists are used to store multiple items in a single variable

fruits = 'apple, mango, banana, peach, orange, grapes, cherry, kiwi, pineapple, pear'
print(type(fruits))

# replace function
var = fruits.replace(' ','').split(',')
print(var)
print(type(var))

# LIST INDEXES and SLICING
print(var[2])
print(var[:2])
print(var[-2])
print(var[4:])
# list indexing and slicing is same as string

# APPEND (ADDING ELEMENTS IN A LIST IN THE END)
var.append('strawberry')
print(var)

# INSERT (ADDING AT A PARTICULAR LOCATION - index, value)
var.insert(0,'avacado')
print(var)

# CHANGING AN ELEMENT
var[7] = 'berry'
print(var)

# REMOVING AN ELMENT
# POP -> RETURN LAST ELEMENT and REMOVE IT FROM LIST
print(var.pop())
print(var)
# BY DEFAULT -1 last element otherwise provided index element
print(var.pop(3))
print(var)

# REMOVE -> CASE SENSITIVE REMOVAL
var.remove('apple')
print(var)