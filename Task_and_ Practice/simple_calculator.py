print("Enter a number: ")
num1 = int(input())
print("Enter another number: ")
num2 = int(input())
print("Select an operation to perform ->")
print("1.Addition")
print("2.Substration")
print("3.Multiplication")
print("4.Division")
print("5.Average")
print("6.Square")
print("7.Cube")
op = int(input())

if(op==1):
    sum = num1 + num2
    print(f"Additon of {num1} and {num2} is {sum}") #This is an another method to print string and variable together using f-string of python
elif(op==2):
    sub = num1 - num2
    print(f"Substration of {num1} and {num2} is {sub}")
elif(op==3):
    mul = num1 * num2
    print("Multiplication of " + str(num1)+ " and " +str(num2)+ " is " +str(mul) )  #Here we have used str() function to convert integer to string and used in a print statement to print it properly
elif(op==4):
    if(num1 > num2):
        div = num1/num2
    else:
        div = num2/num1
    print(f"Division of {num1} and {num2} is {div}")
elif(op==5):
    avg = (num1+num2)/2
    print(f"Average of {num1} and {num2} is {avg}")
elif(op==6):
    square1 = num1**2
    square2 = num2**2
    print(f"Square of {num1} is {square1}")
    print(f"Square of {num2} is {square2}")
elif(op==7):
    cube1 = num1**3
    cube2 = num2**3
    print(f"Cube of {num1} is {cube1}")
    print(f"Cube of {num2} is {cube2}")
else:
    print("Invalid operator")