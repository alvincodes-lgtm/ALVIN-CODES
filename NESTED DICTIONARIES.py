

dictionary = {
        "name": "Joe",
        "age": 18
}

print(dictionary["name"]) 

#.get()

student = {
    "name": "Alvin",
    "School": "JKUAT",
    "course": "Computing"
}

print(student)

#Adding new items.
student["Email"] = "Alvin012@gmail.com"
student["Phone"] = "0798765432"

print(student)

student.pop("course")  

print(student)

del student["School"]

print(student)

print("Keys: ")
for key in student.keys():
    print(key)

print("\nValues: ")
for value in student.values():
    print(value)

print("\nKeys and Values: ")
for key, value in student.items():
    print(f"{key}: {value}")


#Nested Dictionary
Students = {
    "student1": {
        "name": "Alvin",
        "age": 18
    },
    "student2": {
        "name": "Job",
        "age": 22
    },
    "student3": {
        "name": "Ivan",
        "age": 17
    }
}

#Accessing the information
print("student1 Name: ",
Students["student1"]["name"])

