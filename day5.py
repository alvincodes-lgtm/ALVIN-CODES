#getting users inputs
#input, output & type conversion
#output
print("python day5")

#users input
name = input("enter your name")
print("what's up " + name)

# F SRINGS
#easier to read
#no need to convert data types manually
#you can include operators (+/-)

age = input("when were you born?")
print (f"you are {2026 - int(age)} years old")

height = input("what is your height in meters?")
print (f"your height is {float(height)} meters")

#TYPE CONVERSION
#changes the value from one data type to another

age = 18
print(float(age))

#STRINGS AND INDEXING

county = "Nairobi"
print(county[0])
print(county[1])
print(county[-1])
print(county[:4])

name = "alvin munene"
print(name.upper())
print(name.lower())
print(name.replace("alvin" , "ALVIN"))

