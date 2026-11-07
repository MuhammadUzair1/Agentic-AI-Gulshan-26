# FOR LOOPS

# RANGE
# RANGE (start, end, step/interval)
# DEFAULT START VALUE -> 0
# DEFAULT STEP VALUE -> 1


for num in range(1,10,1):
    print(num)

print('\n\n')

for num in range(10,1,-1):
    print(num)
    
print('\n\n')
    
# LOOP ON LIST
lst = ['a','b','c','d','e','f','g','h']

# OPTION 1:
for i in range(len(lst)):
    print(lst[i], "index", i)
print('\n')
# OPTION 2:
for i in lst:
    print(i)
    
print('\n\n')
    
# LOOP ON STRING
string = 'MUHAMMAD UZAIR'
for i in string:
    if i==' ':
        continue
    elif i.lower() == 'u':
        print('UZAIR')
        continue
    elif i.lower() == 'i':
        break
    print(i)
    
print('\n\n')
    
# NESTED FOR LOOP:
fruits=['apple','guava','banana','grapes','kiwi']
for i in lst:
    print(i)
    if i == 'f':
        for j in fruits:
            if j == 'grapes':
                continue
            print(j)
            
                