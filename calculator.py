def sum(a,b):
    return a+b

def minus(c,d):
    return c-d

def multi(e,f):
    return e*f

def div(g,h):
    return g//h

oper = input("Enter the operation: \n")
num1 = int(input("Enter number 1: \n"))
num2 = int(input("Enter number 2: \n"))

if oper=="+":
    print(sum(num1, num2))

if oper=="-":
    print(minus(num1, num2))

if oper=="*":
    print(multi(num1, num2))

if oper=="/":
    print(div(num1, num2))