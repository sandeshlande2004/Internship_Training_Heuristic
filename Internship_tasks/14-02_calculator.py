title = "Python Based Simple Calculator"
print(title.center(50, '-'))

def add(p, q):
    return p + q

def sub(p, q):
    return p - q

def mul(p, q):
    return p * q

def div(p, q):
    return p / q
    
def sq(p):
    return p**2

def cube(p):
    return p**3

def sqrt(p):
    return p**0.5

def cbrt(p):
    return p**(1/3)

def expo(p, n):
    return p**n

def fact(p):
    if p == 0:
        return 1
    else:
        return p * fact(p-1)

def main():
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Cube")
        print("7. Square Root")
        print("8. Cube Root")
        print("9. Exponential")
        print("10. Factorial")
        print("11. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 11:
            break
        elif choice == 1:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print("The sum is: ", add(num1, num2))
        elif choice == 2:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print("The difference is: ", sub(num1, num2))
        elif choice == 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            print("The product is: ", mul(num1, num2))
        elif choice == 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if(num2 == 0):
                return print("Denominator cannot be zero !!")
            else:
                print("The division is: ", div(num1, num2))
        elif choice == 5:
            num = int(input("Enter the number: "))
            print("The square is: ", sq(num))
        elif choice == 6:
            num = int(input("Enter the number: "))
            print("The cube is: ", cube(num))
        elif choice == 7:
            num = int(input("Enter the number: "))
            print("The square root is: ", sqrt(num))
        elif choice == 8:
            num = int(input("Enter the number: "))
            print("The cube root is: ", cbrt(num))
        elif choice == 9:
            num1 = int(input("Enter the base: "))
            num2 = int(input("Enter the power: "))
            print("The result is: ", expo(num1, num2))
        elif choice == 10:
            num = int(input("Enter the number: "))
            print("The factorial is: ", fact(num))
        else:
            print("Invalid choice !!")
        
if __name__ == "__main__":
    main()