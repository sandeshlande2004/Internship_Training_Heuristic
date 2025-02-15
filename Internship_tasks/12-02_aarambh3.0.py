# Aarambh 3.0

title = 'Welcome to Aarambh 3.0'
print(title.center(50))
print("-------------------------------------------------------------")

name = str(input("Please enter your name: "))
print("-------------------------------------------------------------")
print("1.Overarm\n2.Underarm\n3.Indoor\n4.Traditional\n5.Group\n6.Kratex")
print("-------------------------------------------------------------")
print("Enter your choice: ")
choice = str(input())


if(choice == 'Overarm'):
    print("Visit to outside ground")
    
    age = int(input("Enter your age: "))
    
    if(age < 0):
        print("Invalid input age")
    elif(age <= 20):
        print("Goto section A")
    else:
        print("Goto section B")
    
elif(choice == 'Underarm'):
    print("Visit inside ground")
    
    age = int(input("Enter your age: "))
    
    if(age < 0):
        print("Invalid input age")
    elif(age <= 20):
        print("Goto section A")
    else:
        print("Goto section B")

elif(choice == 'Indoor'):
    print("Visit to 1st floor")
    
    age = int(input("Enter your age: "))
    
    if(age < 0):
        print("Invalid input age")
    elif(age <= 20):
        print("Goto section A")
    else:
        print("Goto section B")

elif(choice == 'Traditional'):
    print("Visit Engineering Building")
    
    age = int(input("Enter your age: "))
    
    if(age < 0):
        print("Invalid input age")
    elif(age <= 20):
        print("Goto section A")
    else:
        print("Goto section B")

elif(choice == 'Group'):
    print("Visit Pharmacy Building")
    
    age = int(input("Enter your age: "))
    
    if(age < 0):
        print("Invalid input age")
    elif(age <= 20):
        print("Goto section A")
    else:
        print("Goto section B")

elif(choice == 'Kratex'):
    print("Visit to campus for DJ night (KRATEX)")
    
    age = int(input("Enter your age: "))
    
    if(age < 0):
        print("Invalid input age")
    elif(age <= 20):
        print("Goto section A")
    else:
        print("Goto section B")

else:
    print("You made an invalid choice")

print("-------------------------------------------------------------")
print(f"Thank you for participating in Aarambh 3.0 *{name}*.\n You have participated in *{choice}* event.")