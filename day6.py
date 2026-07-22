#decision making & comparison operators
# COMPARISON OPERATORS
# = - equal to
# ! - not equal to
# > - greater than
# < - less than
# >= - greater than or equal to
# <= - less than or equal to

# IF STATEMENTS

age = 12
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")
   
   
 # if...elif...else statements

score = 85
if score >= 90:
    print("A")

elif score > 80:
   print("B")

elif score > 70:
    print("C")

else:
    print("FAIL")
     
# LOGICAL OPERATORS
#and
#or 
#not

age = 20
is_available = True

if age >= 18 and is_available:
    print("you can vote")

else:
    print("cannot vote")

    if not is_available:
        print("cannot vote")
