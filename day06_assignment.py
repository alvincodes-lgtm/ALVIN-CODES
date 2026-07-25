# ATM
name = input("enter your name ")
password = input("password ")
balance = input("enter your balance ")

if name ==  "alvin" and password == "qwerty" and balance == "10000":
    print("Welcome Back")
    print("balance: " + str(balance))

elif name != "alvin":
    print("unknown user")

elif balance != "10000":
    print("wrong balance")


else:
    print("incorrect password")



    