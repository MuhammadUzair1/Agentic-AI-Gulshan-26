# LISTS CONTINUE
# LISTS ARE MUTABLE AND ORDERED
# RECAP
fruits = ['apple', 'mango']
fruits.append("orange")
fruits[1] = 'cheery'
fruits.insert(2,'grapes')
fruits.pop() # LAST ELEMENT REMOVED
fruits.pop(1) # INDEX 1 ELEMENT WILL BE REMOVED
fruits.remove('grapes') # REMOVE WITH EXACT KEY MATCH 
print(fruits)

fruits_2 = ['watermelon', 'guava', 'kiwi']
# EXTEND
fruits.extend(fruits_2)
print(fruits)

# REVERSE THE LIST
fruits.reverse()
print(fruits)

# CLEAR LIST -> EMPTY THE WHOLE LIST
# fruits.clear()
# print(fruits)

# SORT
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# COPY
# SOFT COPY - SHALLOW COPY
fruits_copy = fruits
print(fruits_copy.pop())
print(fruits_copy)
print(fruits)
# HARD COPY - DEEP COPY
fruits_copy = fruits.copy()
fruits_copy.append('banana')
print(fruits)
print(fruits_copy)

# LENGTH OF THE LIST
print(len(fruits))
print(len(fruits_copy))
print(type(len(fruits)))


