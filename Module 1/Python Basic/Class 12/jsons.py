"""
================================================================
 Module 1 - Python Basics | Class 12 (Part 2): JSON
================================================================

JSON = JavaScript Object Notation.

It is the most common format for SENDING and SAVING data as text.
Websites, mobile apps and AI tools (like ChatGPT / Claude APIs)
send their data to each other in JSON.

JSON looks almost exactly like a Python dictionary:

    {
        "name": "Uzair",
        "age": 25,
        "skills": ["Python", "SQL"],
        "is_student": false
    }

But remember: JSON is just TEXT (a string). To work with it in
Python we convert it to a dictionary, and back again.

    Python dict  --- json.dumps() --->  JSON text
    JSON text    --- json.loads() --->  Python dict

    (Easy way to remember: the 's' at the end means 'string')

Topics covered in this file:
    1. Python dictionary -> JSON string    json.dumps()
    2. JSON string -> Python dictionary    json.loads()
    3. How Python types change in JSON
    4. Making JSON pretty: indent and sort_keys
    5. Reading a real JSON file: Nobel Prize winners   json.load()
    6. Practice examples
"""

import json


# ==============================================================
# 1. PYTHON DICTIONARY -> JSON STRING:  json.dumps()
# ==============================================================
person = {
    'name': 'Uzair',
    'gender': 'Male',
    'age': 25,
    'mobile': '03001234567',
    'address': {
        'city': 'Karachi',
        'province': 'Sindh',
        'country': 'Pakistan'
    }
}

print('Type of person:', type(person))      # <class 'dict'>

json_text = json.dumps(person)
print('Type of json_text:', type(json_text))    # <class 'str'>
print(json_text)
print()

# Since it's a string now, dictionary tricks DON'T work on it:
# json_text['name']   -> TypeError


# ==============================================================
# 2. JSON STRING -> PYTHON DICTIONARY:  json.loads()
# ==============================================================
# Imagine we received this text from a website:
response = '{"city": "Lahore", "temperature": 31, "is_raining": false}'

weather = json.loads(response)
print(type(weather))                # <class 'dict'>
print(weather['city'])              # Lahore
print(weather['temperature'])       # 31
print(weather['is_raining'])        # False  (JSON false -> Python False)
print()


# ==============================================================
# 3. HOW PYTHON TYPES CHANGE IN JSON
# ==============================================================
#   | Python          | JSON            |
#   |-----------------|-----------------|
#   | dict            | object  { }     |
#   | list, tuple     | array   [ ]     |
#   | str             | string  "..."   |
#   | int, float      | number          |
#   | True / False    | true / false    |
#   | None            | null            |
#
# Also: JSON ALWAYS uses "double quotes", never 'single quotes'.

examples = {
    'a_list': [1, 2, 3],
    'a_tuple': (4, 5),
    'yes': True,
    'no': False,
    'nothing': None,
    'price': 99.5
}
print(json.dumps(examples))
# {"a_list": [1, 2, 3], "a_tuple": [4, 5], "yes": true, "no": false, "nothing": null, "price": 99.5}
print()


# ==============================================================
# 4. MAKING JSON PRETTY: indent AND sort_keys
# ==============================================================
# indent=4     -> puts each item on its own line, 4 spaces deep
# sort_keys    -> puts the keys in A-Z order

print(json.dumps(person, indent=4))
print()
print(json.dumps(weather, indent=2, sort_keys=True))
print()


# ==============================================================
# 5. READING A REAL JSON FILE: NOBEL PRIZE WINNERS
# ==============================================================
# json.load()  (no 's')  -> reads JSON from a FILE
# json.dump()  (no 's')  -> writes JSON to a FILE
#
# We use open() and 'with' to open the file.
# (We will learn file handling in detail in Class 13.)
#
# The file 'nobel-prize-winners-by-year.json' looks like this:
# [
#   {
#     "year": "1901",
#     "winners": [
#       {
#         "category": "chemistry",
#         "winners": [ {"name": "...", "country": "...", "achievement": "..."} ]
#       },
#       ...
#     ]
#   },
#   ...
# ]

import os

# Find the JSON file in the SAME folder as this Python file,
# so it works no matter which folder your terminal is in.
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, 'nobel-prize-winners-by-year.json')

with open(file_path, 'r', encoding='utf-8') as file:
    nobel = json.load(file)         # now 'nobel' is a normal Python list

print('Type:', type(nobel))                         # <class 'list'>
print('Number of years in the file:', len(nobel))
print('First year:', nobel[0]['year'])
print('Last year :', nobel[-1]['year'])
print()

# --- Winners of the very first Nobel Prizes (1901) ---
first_year = nobel[0]
print('Nobel Prize winners in', first_year['year'])
for prize in first_year['winners']:
    for winner in prize['winners']:
        print('  ', prize['category'].title(), '->', winner['name'], '(' + winner['country'] + ')')
print()


# ==============================================================
# 6. PRACTICE EXAMPLES
# ==============================================================

# --- Find all the Nobel Prize winners from Pakistan ---
print('Nobel Prize winners from Pakistan:')
for year in nobel:
    for prize in year['winners']:
        for winner in prize['winners']:
            if winner['country'] == 'Pakistan':
                print('  ', year['year'], '-', winner['name'], '-', prize['category'])
print()

# --- Count the total number of winners in the file ---
total = 0
for year in nobel:
    for prize in year['winners']:
        total += len(prize['winners'])
print('Total winners in the file:', total)
print()

# --- Shopping cart: dict -> JSON -> dict ---
cart = {'customer': 'Sara', 'items': ['Shoes', 'Bag'], 'paid': False}
cart_json = json.dumps(cart)           # send it to a server
print('Sent    :', cart_json)
received = json.loads(cart_json)       # the server reads it back
print('Received:', received['customer'], 'bought', len(received['items']), 'items')
