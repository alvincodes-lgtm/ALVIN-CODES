students= [
    {"name": "Williams", "age": 21, "major": "mechanical eng", "score": 70},
    {"name": "Nathan", "age": 19, "major":"pharmacy", "score": 65},
    {"name": "James", "age": 20, "major":"IT", "score": 75},
    {"name": "Emily", "age":18, "major":"Computer Science", "score":60},
    {"name": "Joy", "age":19, "major" :"chemistry", "score":72},
]

def display_students(students):

    for students in students:

        print(
            f"{students['name']} |"
            f"{students['major']} |"
            f"{students['score']}|"

        )

display_students(students)

