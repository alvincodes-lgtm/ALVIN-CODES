#Accessing values in a dictionary using functions

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

#store function results in a dictionary

message = {
    "Hello": greet("John"),
    "Goodbye": farewell("Alice")
}

#access dictionary values
print(message["Hello"])
print(message["Goodbye"])

#JSON
#JavaScript object Notation

{
    "name": "Alvin",
    "age": 18,
    "city": "washington"
}

#converting a dictionary to JSON

import json
student = {
    "name": "Alvin",
    "age": 18,
    "city": "washington"
}
data = json.dumps(student)
print(data)

import json
data = '{"name": "Alvin", "age": 18, "city": "washington"}'
#Converting JSON to a dictionary
student = json.loads(data)
print(data)