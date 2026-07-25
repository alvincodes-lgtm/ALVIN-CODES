#loops
#while loop
#cake = 10 
#while cake <= 9:
  #   print ("cake")
     

#infinite loops
#cake = 10
#while cake <= 9:
 #     print ("cake")

#for loops
#repeat over a sequence
 
for numbers in range (7):
      print(numbers) 

#range

for i in range (5):
      print(i)

for i in range (0,12,2):
            print(i)

#looping through strings
for letters in "PYTHON":
       print(letters)

#BREAK
#stops the loop imediately

for i in range (1,11):
       if i == 6:
              break
       print (i)

#continue
#skips one iteration

for i in range (1,11):
       if i == 5:
              continue
       print(i)

#PASSWORD CHECKER

password = ""
while password != "*****": 
       password = input("Enter Password")
print("welcome")
