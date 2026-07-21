first_name = "alvin"
last_name = "munene"
age = "18"
height = "169"
weight = "68"
university = "jomo kenyatta university of agriculture and technology"
course = "computer engineering"

def myfunc():
    global course
    course = "software engineering"

myfunc()
print ("FIRST_NAME : " , first_name)
print ("LAST_NAME : " , last_name)
print ("AGE : " , age)
print ("HEIGHT : " , height)
print ("WEIGHT : " , weight)
print ("UNIVERSITY : " , university)
print ("COURSE : " , course) 

type(function(first_name))