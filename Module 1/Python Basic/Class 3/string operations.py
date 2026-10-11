import os

course = 'Agentic AI'
print(course)

description = '''
I'm Muhammad Uzair Khan, a Data Engineer, AI Engineer, and Data Scientist with a 
passion for cloud computing, scalable data solutions, and
AI-driven applications. I specialize in building 
high-performance data pipelines, real-time streaming solutions, 
and AI-powered systems that drive efficiency and innovation. 🚀
'''
print(description)

# STRING OPERATIONS
# UPPER
print(course.upper())
# LOWER
print(course.lower())
# TITLE CASE
print(course.title) # THIS RETURNS MEMORY/FUNCTION ADDRESS
print(course.title()) 
# ISLOWER
print(course.islower())
# ISNUMERIC -> Returns True when only have numbers
print(course.isnumeric())
# ISAPLHA -> Returns True when only have alphabets
print(course.isalpha())
print('UZAIR'.isalpha())

# TESTING
var = '123'
# var = 123 
# this will return error as string operations only work on strings
print(var.isnumeric())

os.system('cls')
# SLICING
print(course)
# course -> Agentic AI
#           0123456789
#                 -2-1

print(course[0])
print(course[9])
print(course[-1])
# print(course(7)) # ONLY SQUARE BRACKETS ARE USED FOR SLICING
print(course[7])

# RANGE SLICING
# [start:end:interval]

print(course[0:7]) # GETTING WORD AGENTIC
print(course[0:8])
print(course[0:9])
print(course[-6:-3])
print(course[-3:-6]) # WRONG RANGE INPUT HENCE EMPTY OUTPUT

# [included, excluded]

# START TO AN INDEX
print(course[:6])
print(course[:-5])

# INDEX TO AN END
print(course[7:])
print(course[-3:])

# GETING ALL
print(course[::])
print(course[:],'\n',end='\n\n')

# INTERVAL
print(course[::2])
print(course[::3])
print(course[2:-3:3])

print(course[0],[8]) # LOGICAL ERROR

# print(course[0:3,7:9]) # ERROR
print(course[:3],course[7:])
print(course[:3]+course[7:])

# ENDING STATEMENT IN PRINT
print(course[:3],course[7:])
print('CLASS END')