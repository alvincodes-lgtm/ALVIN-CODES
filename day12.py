#FUNCTIONS
#re usable block of code that performs a specific task
#WhatsApp
#press send
#send_message()


def Welcome():
    print("Welcome to the program")

Welcome()
Welcome()

#functions with parameters
def greet (name):
    print(f"hello {name}")

greet("Alvin")

#multiple parameters
def introduce(name, age):
    print(f"my name is {name} and I am {age} years old")

introduce("Alvin", 18)
introduce("Roy", 22)

#return values from a function
def add_numbers(a,b):
    print(a+b)

add_numbers(5,10)
#print(add_number)

#with return function
def add_number (a,b):
    return a+b

#result = odd_numbers(5,10)
#print(result)



#PRINT                          VS             RETURN
#displays info on the screen                sends info back to the caller
#cannot be reused                            can be reused
#used for output only                        used for output and further processing
