def hello():
    print("hello")
    hello()

#every recursive function needs a condition that tells it when to stop
#the condition is called base case

def countdown(n):

    if n == 0:
         print("happy new year!")
         return

    print(n)

    countdown(n - 1)

countdown(5)

