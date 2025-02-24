title = "Welcome to Aarambh 3.0 2025 by Indala Institute of Technology"
print(title.center(100))
print("-"*115)

name = input("Enter your name: ")


while(1): # Infinite loop like while True
    print("\nEvents:")
    print("\n1.DJ Night\n2.Dance\n3.Singing\n4.Days\n")
    print("-------------------------------------------------------------")
    
    choice = int(input("Enter your choice: "))
    
    if(choice == 1):
        print("Come to Engineering Building")
        age = int(input("Enter your age: "))
        if(age < 0):
            print("Invalid input age")
        elif(age <= 18):
            print("Show id card")
        else:
            print("You can enter")
        break
        
    elif(choice == 2):
        print("Come to 1st floor")
        gen = input("Enter your gender: ").lower()
        if(gen == "Male"):
            print("Visit to left room")
        else:
            print("Visit to right room")
        break
        
    elif(choice == 3):
        print("Come to 2nd floor")
        gen = input("Enter your gender: ").lower()
        if(gen == "Male"):
            print("Visit to left room")
        else:
            print("Visit to right room")
        break
    
    elif(choice == 4):
        print("Come to Pharmacy Building")
        break
    
    else:
        print("Invalid choice")
        print("Please enter valid choice again")
        
print(f"\n{name}, Please enjoy the event")
print("\nThank you for visiting Aarambh 3.0 2025")
    