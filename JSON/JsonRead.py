# To work with json IMPORT JSON!!!
import json
# This is the Excel data (no keys)
filename = 'people2.json'
# Open the file (standard file open stuff)
with open(filename, 'r', encoding='utf-8', newline='') as f:
# Load the whole json file into an object named people
    people = json.load(f)

print(type(people))
print(people)

for p in people:
    print(p['ID'], p['Name'], p['Age'])