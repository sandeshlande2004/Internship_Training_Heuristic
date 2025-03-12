class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        print(f"Addition of {self.a} and {self.b} is {self.a + self.b}")
    
    
class sub:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def substration(self):
        print(f"Subtraction of {self.a} and {self.b} is {self.a - self.b}")

class mul:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def multiplication(self):
        print(f"Multiplication of {self.a} and {self.b} is {self.a * self.b}")

class div:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def division(self):
        print(f"Division of {self.a} and {self.b} is {self.a / self.b}")

obj_1 = add
obj_2 = sub
obj_3 = mul
obj_4 = div

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '5':
        break
    elif choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        obj_1 = add(num1,num2)
        obj_1.addition()
        break
    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        obj_2 = sub(num1,num2)
        obj_2.substration()
        break
    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        obj_3 = mul(num1,num2)
        obj_3.multiplication()
        break
    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        obj_4 = div(num1,num2)
        obj_4.division()
        break
    else:
        print("Invalid choice")
        
