#http - Hypertext Transfer Protocol
# a set of rules which allow computers to communicate over the internet
#https://jobsy.co.ke

#https://google.com

#HTTP request and response

#Request - It what your computer ask the server for

#Response - what the server sends back

#Browser - Request - Server
#Browser - Response - Server

#Server - is a computer that provides something to other computers

#API - Application Programming Interface
    #  It allows a program communicate to other program

#https://example.com/api/jobs
[
    {
        "title": "Python Developer",
        "Company": "Safaricon PLC"
    },
    {
        "title": "Data Analyst",
        "company": "IBM"    
    },
]

 #HTTP Methods

 #GET- Get Information
 #POST- Send/ Create information
 #PUT- Update information
 #PATCH - Partially update informnation
 #DELETE - Delete Information

 #POST Request
 #POST /Users
#{
  # "name": "Alvin"
   #"email": "alvine@mail.com"
#}

#HTTP Status Codes
#200-Ok
#201-Created
#400-Bad Request
#403-You don't have permission
#404-Not Found
#500-Internal Server Error

#How to make a https request in python

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

data = response.json()

print(data)