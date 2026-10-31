# SETS
# SETS ARE IMMUTABLE AND UNORDERED

this_set = {'apple', 'mango','orange'}
print(type(this_set))


dup_list = [1,2,3,1,5,6,3]
print(dup_list)

myset = set(dup_list)
mylist = list(myset)
print(mylist)

print(len(this_set))

this_set.add('grape')
print(this_set)

print(this_set.pop())
print(this_set)

this_set.remove('apple')
print(this_set)





