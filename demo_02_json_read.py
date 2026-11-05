import json

try:
    with open("many_people.json", "r") as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("JSON File not found")
except json.decoder.JSONDecodeError:
    print("That JSON file is not legit!")

#print out nami and navigator
print(data[0]["name"], data[0]["job"])

# print luffy's age:
print(data[2]["age"])
