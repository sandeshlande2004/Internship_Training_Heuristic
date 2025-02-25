#Problem statement: Input number from user and add it to intially set variable 'a' and after that again take input from user and add it to the result of previous addition
# like a = 10 1st add : a + b(10)(input from user)= 20 then 2nd add : 1st add result + b(20)(input from user) = 40

a = 10

# while True:
#     print("\n1.Start\n2.Stop")
#     choice = int(input("Enter your choice: "))
    
#     if choice == 1:
        
#         num = int(input("Enter your number: "))
#         result = a + num
#         print(f"Result: {result}")
#         a = result // a += num and print 'a' only
        
#     elif choice == 2:
#         print("You have stop the addition loop !")
#         break
    
#     else:
#         print("Invalid choice. Please choose 1 or 2.")
#         print("Please try again!!")
    

while (1):
    print("\n1.Start\n2.Stop")
    b = input("Enter a no.: ")
    if b == "Stop":
        print("Program stopped !!")
        break
    elif b != "Stop":
        c = int(b)  #typecasting (string is converted into int )
        a += c #instead of doing a = result we can directly add the value to 'a' and print 'a'
        print(f"Result: {a}")
        