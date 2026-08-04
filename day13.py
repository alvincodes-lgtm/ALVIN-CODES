#function Argument & scope
#learning to make function more smarter

def order_pizza(size, toppings):
    print(f"{size} pizza with{toppings}")

order_pizza("large", "pepperoni and mushrooms")


#positional argumnts
def student(name, age):
    print(name, age)



#keyword arguments
#lets us specify the value that belongs to a parameter
student(age=18 , name="Alvin")

#default arguments
def pay(amount, currency ="Ksh"):
    print(f"pay{amount} in {currency}")
pay(500)
pay(500,"USD")

#scope
#scope, earns the region of a program where a variable is accessible. 
# there are two types of scope ;local and global

#local scope
def test():
    x=10
    print(x)

test()

#global scope
school = "Kagumo High"
def print_school():
    print(school)

print_school()