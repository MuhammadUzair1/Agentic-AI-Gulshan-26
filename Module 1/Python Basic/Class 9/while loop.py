# PYTHON HAS 2 TYPES OF LOOPS
# - WHILE LOOP
# - FOR LOOP


# WHILE LOOP
num = 1
while num<10:
    # LOOP BODY 
    print(num)
    num = num + 1
    # LOOP BODY END
    
print('END\n\n\n')


# BREAKS IN LOOP
num = 1
while num<10:
    # LOOP BODY 
    print(num)
    if num == 5:
        print("BREAK")
        break
    num = num + 1
    # LOOP BODY END
    
print('END\n\n\n')


# CONTINUE IN LOOP
num = 1
while num<10:
    # LOOP BODY 
    num = num + 1
    print(num)
    if num == 5:
        continue
    # num = num + 1
    # LOOP BODY END
    
print('END')

# ELSE IN LOOP
num = 1
while num<10:
    # LOOP BODY 
    print(num)
    num = num + 1
    # LOOP BODY END
else:
    print('LOOP ENDED :\'(')
    
print('END\n\n\n')