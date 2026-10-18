# TUPLES
# TUPLES ARE ORDERED AND IMMUTABLE

mytuple = (12,354,6,92,'abc')
print(type(mytuple))
print(mytuple)

# TUPLE IS ORDERED
print(mytuple[0:2])
# ORDERING AND SLICING IS EXACTLY SAME AS LISTS
# CHANGING A ALREADY FILLED INDEX IS NOT POSSIBLE
# mytuple[0] = 1

# TUPLE CAN HAVE DUPLICATE VALUES
tuple2 = (1,1,2,3)
print(tuple2)
print(len(tuple2))

# ADDING ELEMENTS IN TUPLE
mytuple = list(mytuple)
mytuple.append('xyz')
mytuple = tuple(mytuple)
print(mytuple)

# TUPLE UNPACKING
print(tuple2)
(a, b, c , d) = tuple2
print(a)
print(type(a))


fruits = ('apple', 'mango', 'grapes', 'kiwi', 'melon', 'orange')
(x, *y, z) = fruits
print(fruits)
print(x)
print(y)
print(z)

