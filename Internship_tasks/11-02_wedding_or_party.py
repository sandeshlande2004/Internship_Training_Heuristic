entry = str(input("Where do you want to go?\nParty\nWeddinng\nChoice:")).lower()

if(entry == 'party'):
    print("You are going to party")
    print("Enjoy the party")
    print("Go to section A")
elif(entry == 'wedding'):
    print("You are going to wedding")
    print("Enjoy the wedding")
    print("Go to section B")
else:
    print("Invalid choice")