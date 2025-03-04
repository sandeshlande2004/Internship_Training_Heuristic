import operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = operations.add(num1,num2)
print(f"Addition of {num1} and {num2} : {sum}")

difference = operations.sub(num1,num2)
if num1 > num2:
    print(f"Substraction of {num1} and {num2} : {difference}")
else:
    print(f"Substraction of {num2} and {num1} : {difference}")

multiplication = operations.mul(num1, num2)
print(f"Multiplication of {num1} and {num2} : {multiplication}")

division = operations.div(num1, num2)
print(f"Division of {num1} and {num2} : {division}")