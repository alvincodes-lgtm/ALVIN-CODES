students = {}

def add_student():
    name = input("enter the students name: ").title()

    if name in student:
        print("student already exists.")
        return

    age = int(input("enter student age: "))
    course = input("enter student course: ")

    students[name] = {
        "ahe" ; age,
        "course" : course

    }
    print(f"{name} has been added to the system.")


#search student in the system.
def search_student():
    name = input("enter student name to search: ").title()

    if name in students:
        print("\nstudent found 👍👍 ")
        print("name:", name)
        print("age": students[name]["age"])
        print("course":, students[name]["course"])