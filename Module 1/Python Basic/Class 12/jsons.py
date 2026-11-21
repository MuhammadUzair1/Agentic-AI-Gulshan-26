import json

x = {
    'name':'Uzair',
    'gender':'Male',
    'age':'25',
    'mobile':'03112025620',
    'address':{
        'city':'Karachi',
        'province':'Sindh',
        'country':'Pakistan'
    }
}

print("Type of x:", type(x))

# Use json.dumps() to convert the dictionary into a JSON-formatted string
y = json.dumps(x, indent=4) # indent=4 makes it easier to read

print("Type of y:", type(y))
print("JSON String:\n", y)

