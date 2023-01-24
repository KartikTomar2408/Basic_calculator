import os
def add(a,b):
     return a+b
 
def sub(a,b):
     return a-b
 
def prod(a,b):
     return a * b
 
def div(a,b):
     return a / b
 
def si(p, r, t):
    return (p*r*t) / 100
 
def ci(p, r ,t):
    return p * pow((1 + r/100), t)
 
def sqr(num):
    return num**2
 
def sqrt(num):
    return num**0.5

def calculator(prompt):
    os.system('cls')
    if(prompt.lower()=="add"):
        value1 = int(input("Enter first digit : "))
        value2 = int(input("Enter second digit : "))
        return add(value1, value2)
    elif (prompt.lower()=="sub"):
        value1 = int(input("Enter first digit : "))
        value2 = int(input("Enter second digit : "))
        return sub(value1, value2)
    elif (prompt.lower()=="div"):
        value1 = int(input("Enter first digit : "))
        value2 = int(input("Enter second digit : "))
        return div(value1, value2)
    elif (prompt.lower()=="prod"):
        value1 = int(input("Enter first digit : "))
        value2 = int(input("Enter second digit : "))
        return prod(value1, value2)
    elif (prompt.lower()=="si"):
        value1 = int(input("Enter principal : "))
        value2 = int(input("Enter rate : "))
        value3 = int(input("Enter time : "))
        return si(value1, value2, value3)
    elif (prompt.lower()=="ci"):
        value1 = int(input("Enter principal : "))
        value2 = int(input("Enter rate : "))
        value3 = int(input("Enter time : "))
        return ci(value1, value2, value3)
    elif (prompt.lower()=="sqr"):
        value1 = int(input("Enter first digit : "))
        return sqr(value1)
    elif (prompt.lower()=="sqrt"):
        value1 = int(input("Enter first digit : "))
        return sqrt(value1)
os.system('cls')
prompt = input("Select the function you want to perform : \nAddition : add\nSubtraction : sub\nDivision : div\nMultiplication : prod\nSimple Interest : si\ncompound Interest:ci\nSquare : sqr\nSquare root : sqrt\n")
print(calculator(prompt))
    
    
