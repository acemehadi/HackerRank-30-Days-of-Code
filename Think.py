def add(a,b):
    result=a+b
    print(result)

def sub(a,b):
    result=a+b
    print(result)

def multi(a,b):
    result=a*b
    print(result)

def divide(a,b):
    result=a/b
    print(result)

a=int(input("Enter your number"))
b=int(input("enter your another number"))
operator=input("enter your Operator")

if operator=="+":
    add(a,b)
elif operator=="-":
    sub(a,b)
elif operator=="*":
    multi(a,b)
elif operator=="/":
    divide(a,b)
else:
    print("Please enter Valid Operator")