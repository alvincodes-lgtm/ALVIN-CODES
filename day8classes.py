class student:
    def __init__(self,name, course):

        self.name = name
        self.course = course

    def introduce(self):
            print(f"my name is {self.name}")
            print(f"I study {self.course}")

student1 = student ("ALVIN","SOFTWARE")
student2 = student ("MARK","COMPUTER SCIENCE")
student3 = student ("BILL","IT")

student1.introduce()
student2.introduce()
student3.introduce()
