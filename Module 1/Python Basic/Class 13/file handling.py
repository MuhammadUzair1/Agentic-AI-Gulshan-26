"""
================================================================
 Module 1 - Python Basics | Class 13 (Part 1): File Handling
================================================================

Until now, all our data disappeared when the program ended.
With FILE HANDLING our program can:
    - READ data from a file   (e.g. a list of students)
    - WRITE data to a file    (e.g. save a report)
    - ADD (append) to a file  (e.g. a log or a diary)
    - CREATE and DELETE files

The main function is open():

    open(file_path, mode, encoding='utf-8')

Topics covered in this file:
    1. File paths - finding the file correctly
    2. File modes: r, w, a, x
    3. Opening and closing a file
    4. The 'with' statement (the best way)
    5. Reading: read(), readline(), readlines(), looping
    6. Cleaning lines with strip()
    7. Writing: 'w' mode (overwrite)
    8. Appending: 'a' mode (add to the end)
    9. Creating a file: 'x' mode
   10. Checking and deleting files with the os module
   11. Saving and loading JSON files
   12. Practice examples

The file 'sample.txt' in this folder has 10 lines about Python.
We only READ it. All writing happens in 'sample1.txt'.
"""

import os


# ==============================================================
# 1. FILE PATHS - FINDING THE FILE CORRECTLY
# ==============================================================
# If you write   open('sample.txt')   Python looks for the file in
# the folder your TERMINAL is in, not the folder of this .py file.
# That's why the code may work on one computer and fail on another.
#
# Fix: build the full path from the folder of THIS file:
#   __file__                    -> the path of this .py file
#   os.path.dirname(...)        -> the folder that contains it
#   os.path.join(folder, name)  -> folder + file name (correct \ or /)

FOLDER = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(FOLDER, 'sample.txt')      # we only READ this
OUTPUT = os.path.join(FOLDER, 'sample1.txt')     # we WRITE to this
NEW_FILE = os.path.join(FOLDER, 'newfile.txt')   # created and deleted

print('This file is in:', FOLDER)
print()

# TIP: On Windows, if you type a path yourself, use a raw string r'...'
# so the backslashes \ are not treated as escape characters (like \n):
#     r'C:\Users\Uzair\Desktop\notes.txt'


# ==============================================================
# 2. FILE MODES
# ==============================================================
#   | Mode | Name    | What it does                              | File missing? |
#   |------|---------|-------------------------------------------|---------------|
#   | 'r'  | Read    | Read only (DEFAULT mode)                  | ERROR         |
#   | 'w'  | Write   | Write - DELETES old content first!        | Creates it    |
#   | 'a'  | Append  | Adds new content to the END               | Creates it    |
#   | 'x'  | Create  | Creates a NEW file                        | Creates it    |
#   |      |         | (ERROR if the file already exists)        |               |
#   | 'r+' | Read +  | Read AND write (file must exist)          | ERROR         |
#   | 'w+' | Write + | Write AND read (deletes old content)      | Creates it    |
#
# You can also add:
#   't' -> TEXT mode (default)      e.g. 'rt' is the same as 'r'
#   'b' -> BINARY mode for images, PDFs, videos   e.g. 'rb', 'wb'
#
# NOTE: 'rw' is NOT a valid mode. Use 'r+' to read and write.
#
# Always add encoding='utf-8' so special characters (Urdu, emojis,
# quotes like ’ “ ”) are read and written correctly.


# ==============================================================
# 3. OPENING AND CLOSING A FILE
# ==============================================================
f = open(SAMPLE, 'r', encoding='utf-8')
print(f.readline())         # reads the FIRST line
print(f.readline())         # reads the NEXT line (it remembers its place)
f.close()                   # ALWAYS close the file when you are done!

# If you forget close(), the file stays locked/open and changes may
# not be saved. That's why we use 'with' (next section).


# ==============================================================
# 4. THE 'with' STATEMENT (THE BEST WAY)
# ==============================================================
# 'with' closes the file AUTOMATICALLY when the indented block ends,
# even if an error happens inside it.

with open(SAMPLE, 'r', encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

print('Is the file closed now?', f.closed)      # True
print()


# ==============================================================
# 5. READING A FILE
# ==============================================================
#   | Method        | Returns                                  |
#   |---------------|------------------------------------------|
#   | read()        | The WHOLE file as ONE string             |
#   | read(n)       | Only the first n characters              |
#   | readline()    | ONE line (the next one) as a string      |
#   | readlines()   | ALL lines as a LIST of strings           |

# --- read(): the whole file ---
with open(SAMPLE, 'r', encoding='utf-8') as f:
    content = f.read()
print('--- read() ---')
print(content)

# --- read(n): only the first few characters ---
with open(SAMPLE, 'r', encoding='utf-8') as f:
    print('--- read(6) ---')
    print(f.read(6))            # Python
    print()

# --- readlines(): a list of lines ---
with open(SAMPLE, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print('--- readlines() ---')
print('Type:', type(lines))                 # <class 'list'>
print('Number of lines:', len(lines))       # 10
print('First line in the list:', repr(lines[0]))   # notice the \n at the end
print()

# --- Looping over the file: line by line (best for BIG files) ---
print('--- looping ---')
with open(SAMPLE, 'r', encoding='utf-8') as f:
    for line in f:
        print(line)             # notice the EMPTY lines between them! (see section 6)


# ==============================================================
# 6. CLEANING LINES WITH strip()
# ==============================================================
# Every line ends with a hidden NEW LINE character '\n'.
# print() also adds its own new line, so we get an empty line in between.
# .strip() removes spaces and '\n' from both ends of a line.

print('--- looping with strip() ---')
with open(SAMPLE, 'r', encoding='utf-8') as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())
print()

# --- Getting the FIRST WORD of a line ---
# lines[8] -> the 9th line (indexes start at 0)
print('First word of line 9:', lines[8].split(' ')[0])     # Practice
print()


# ==============================================================
# 7. WRITING: 'w' MODE (OVERWRITE)
# ==============================================================
# 'w' creates the file if it doesn't exist.
# WARNING: If the file EXISTS, all its old content is DELETED first!
# write() does NOT add '\n' by itself - add it yourself.

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write('My Python Notes\n')
    f.write('===============\n')

# writelines() writes a whole LIST of strings
topics = ['1. Variables\n', '2. Loops\n', '3. Functions\n']
with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.writelines(topics)

with open(OUTPUT, 'r', encoding='utf-8') as f:
    print('--- sample1.txt after writing ---')
    print(f.read())


# ==============================================================
# 8. APPENDING: 'a' MODE (ADD TO THE END)
# ==============================================================
# 'a' keeps the old content and adds the new content at the END.

with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write('4. File Handling\n')
    f.write('5. Virtual Environments\n')

with open(OUTPUT, 'r', encoding='utf-8') as f:
    print('--- sample1.txt after appending ---')
    print(f.read())

# --- Copying lines from one file into another ---
# Copy only the lines that contain the word 'AI'
with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write('\nLines about AI from sample.txt:\n')
    for line in lines:
        if 'AI' in line or 'Intelligence' in line:
            f.write('- ' + line)          # each line already ends with \n

# --- 'w' DELETES everything: see the difference ---
# (Uncomment these lines to try it. Then sample1.txt will contain
#  ONLY the new text.)
# with open(OUTPUT, 'w', encoding='utf-8') as f:
#     f.write('SAB KHATAM')


# ==============================================================
# 9. CREATING A FILE: 'x' MODE
# ==============================================================
# 'x' creates a NEW, empty file.
# If the file already exists -> FileExistsError
# So we first CHECK if it exists, using os.path.exists().

if not os.path.exists(NEW_FILE):
    with open(NEW_FILE, 'x', encoding='utf-8') as f:
        f.write('I am a brand new file!')
    print('newfile.txt created')
else:
    print('newfile.txt already exists')


# ==============================================================
# 10. CHECKING AND DELETING FILES WITH THE os MODULE
# ==============================================================
#   | Code                        | What it does                   |
#   |-----------------------------|--------------------------------|
#   | os.path.exists(path)        | True if the file/folder exists |
#   | os.path.getsize(path)       | Size of the file in bytes      |
#   | os.listdir(folder)          | List of files in a folder      |
#   | os.remove(path)             | DELETE a file (no recycle bin!)|
#   | os.rename(old, new)         | Rename a file                  |

print('Size of sample.txt:', os.path.getsize(SAMPLE), 'bytes')
print('Files in this folder:', os.listdir(FOLDER))

if os.path.exists(NEW_FILE):
    os.remove(NEW_FILE)
    print('newfile.txt deleted')
else:
    print('The file does not exist')
print()

# --- Handling a missing file with try / except (Class 12) ---
try:
    with open(os.path.join(FOLDER, 'missing.txt'), 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('Sorry, missing.txt was not found!')
print()


# ==============================================================
# 11. SAVING AND LOADING JSON FILES
# ==============================================================
# In Class 12 we learned json.dumps() and json.loads() (strings).
# For FILES we use json.dump() and json.load() (no 's').

import json

student = {'name': 'Sara', 'marks': [85, 90, 78], 'passed': True}
json_path = os.path.join(FOLDER, 'student.json')

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(student, f, indent=4)         # dict -> file

with open(json_path, 'r', encoding='utf-8') as f:
    loaded = json.load(f)                   # file -> dict

print('Loaded from JSON file:', loaded)
print('Average marks:', sum(loaded['marks']) / len(loaded['marks']))

os.remove(json_path)        # clean up (comment this out to see the file)
print()


# ==============================================================
# 12. PRACTICE EXAMPLES
# ==============================================================

# --- Count lines, words and characters in sample.txt ---
with open(SAMPLE, 'r', encoding='utf-8') as f:
    text = f.read()
print('Lines     :', len(text.splitlines()))
print('Words     :', len(text.split()))
print('Characters:', len(text))
print()

# --- Search: which lines mention 'Python'? ---
print("Lines that contain 'Python':")
with open(SAMPLE, 'r', encoding='utf-8') as f:
    for number, line in enumerate(f, start=1):
        if 'Python' in line:
            print(f'  Line {number}: {line.strip()}')
print()

# --- A simple diary: append today's entry with the date ---
from datetime import datetime

diary_path = os.path.join(FOLDER, 'sample1.txt')
with open(diary_path, 'a', encoding='utf-8') as f:
    today = datetime.now().strftime('%d %b %Y, %I:%M %p')
    f.write(f'\n[{today}] Today I learned file handling in Python!\n')
print('Diary entry added to sample1.txt - open it to see!')
