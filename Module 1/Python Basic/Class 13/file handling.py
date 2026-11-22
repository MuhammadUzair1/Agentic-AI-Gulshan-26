# f = open('Module 1\Python Basic\Class 13\sample.txt')

# FILE READ METHODS
# a -> append
# r -> read only
# rw -> read write
# w -> write only

f = open('Module 1\Python Basic\Class 13\sample.txt','rt',encoding='utf-8')
# print(f.read()) # READ WHOLE FILE

print(f.readline())
print(f.readline())
f.close()


# WITH
with open('Module 1\Python Basic\Class 13\sample.txt','rt',encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())


# READLINES
with open('Module 1\Python Basic\Class 13\sample.txt','rt',encoding='utf-8') as f:
    data = f.readlines()
    
# LOOPING ON THE FILE
with open('Module 1\Python Basic\Class 13\sample.txt','r',encoding='utf-8') as f:
    for i in f:
        print(i)
        
        
# READING FIRST WORD FORM A LINE
print()
with open('Module 1\Python Basic\Class 13\sample.txt','rt',encoding='utf-8') as f:
    print(f.readlines()[8].split(' ')[0])
    
    
# APPEND MODE
with open('Module 1\Python Basic\Class 13\sample.txt','a',encoding='utf-8') as f:
    f.write('I am adding lines')
    
# CREATING NEW FILE
with open('Module 1\Python Basic\Class 13\sample1.txt','a',encoding='utf-8') as f:
    for i in data:
        f.write(i+'\n')
    
# OVERWRITE THE FILE
with open('Module 1\Python Basic\Class 13\sample1.txt','w',encoding='utf-8') as f:
    f.write("SAB KHATAM")
    
# CREATE A FILE IF NOT EXIST
import os
if not os.path.exists(r'Module 1\Python Basic\Class 13\newfile.py'):
    f = open(r'Module 1\Python Basic\Class 13\newfile.py','x')
    

# REMOVE FILE
import os
if os.path.exists(r'Module 1\Python Basic\Class 13\newfile.py'):
    os.remove(r'Module 1\Python Basic\Class 13\newfile.py')
