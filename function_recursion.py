def num(n):
    if n==4:
        print("1")
        return
    print("A")
    num(n-1)
    print("B")
    num(n-1)
num(6)

def add(a,b):
    print(a+b)
add(10,20)

def add(a=5,b=10):
    print(a+b)
add()

def num(n):
    if n==4:
        return
    print("4")
    num(n-1)
    print("5")
    num(n-1)
num(6)

def fun(n):
    if n == 1:
        print("A")
        return
    print("B")
    fun(n-1)
    print("C")
    fun(n-1)

fun(3)

def show (n):
    if n==1:
        print("P")
        return
    print("Q")
    show(n-1)
    print("R")
show(3)