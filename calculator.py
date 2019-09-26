from math import *
def multiply(int1, int2):
    return int1*int2
def divide(int1, int2):
    return int1/int2
def add(int1, int2):
    return int1+int2
def subtract(int1, int2):
    return int1-int2
def power(int1, int2):
    return int1 ** int2
print("********************************************")
print("*** Welcome to a rudimentary calculator! ***")
print("********************************************")
print()
cont = "Y"
while(cont == "Y"):
    x = input("Give me the first number: ")
    y = input("Give me the second number: ")
    while(not x.isdigit()):
        x = input("Give me another first number: ")
    while(not y.isdigit()):
        y = input("Give me another second number: ")
    int1 = int(x)
    int2 = int(y)
    calculate = input("Choose one of the five functions (+, -, /, *, ^): ")
    list = ["+", "-", "*", "/", "^"]
    while(calculate not in list ):
        print("Give me a proper function")
        calculate = input("Choose one of the five functions (+, -, /, *, ^): ")
    else:
        if(calculate == "+"):
            print(int1,"+",int2,"is",str(add(int1, int2)))
        elif(calculate == "-"):
            print(int1,"-",int2,"is",str(subtract(int1, int2)))
        elif(calculate == "*"):
            print(int1,"*",int2,"is",str(multiply(int1, int2)))
        elif(calculate == "/"):
            print(int1,"/",int2,"is",str(divide(int1, int2)))
        elif(calculate == "^"):
            print(int1,"^",int2,"is",str(power(int1, int2)))
        cont = input("Do you want to continue using the calculator (Y/N): ")
        if(cont != "Y" and cont != "N"):
            cont = input("Do you want to continue using the calculator (Y/N): ")
        
