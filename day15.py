#recursion
#a recalling function until the base case is reached
def countdown(n):
    if n == 0:
        return

    print(n)

    countdown(n - 2)

countdown(6)  

def hello(times):
    if times == 0:
        return

    print("Hello")

    hello(times - 1)

hello(5)

def countdown(n):
    print(n)
    countdown(n - 1)


