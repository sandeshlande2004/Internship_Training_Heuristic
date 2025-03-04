def add(a,b):
    return a+b

def sub(a,b):
    if a>b:
        return a-b
    else:
        return b-a

def mul(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: Division by zero is not allowed"