"""
JSON (Javascript Object Notation) is a popular format for storing structured data
It uses key-value pairs similar to: dictionaries in python
examole:
{
    "name": "Nami",
    "age": 35,
    "job": "Pirate"
}

in python to work with json, you may need to import json
"""
import json
#writing json to file:
person = {
    "name": "Nami",
    "age": 35,
    "job": "Pirate"
}

file_path = "people.json"

with open(file_path, "w") as file:
    json.dump(person,file, indent=4)

print(f"JSON file ({file_path}) created successfully")

many_people = [
    {
    "name": "Nami",
    "age": 21,
    "job": "navigator"
    },
    {
    "name": "Jace",
    "age": 53,
    "job": "Banker"
    },
    {
    "name": "Luffy",
    "age": 19,
    "job": "Pirate captin"
    }
]

with open("many_people")