while True:
    print("1. Sedan\n2. SUV")
    car_choice = int(input("Enter your car choice: "))
    
    if car_choice == 1:
        while True:
            print("1. 2-Tyre\n2. 4-Tyre")
            tyre_choice = int(input("Enter your tyre choice: "))
            if tyre_choice == 1:
                import sedan
                import two_tyres
                break
            elif tyre_choice == 2:
                import sedan
                import four_tyres
                break
            else:
                print("You can only select 2 or 4 tyre setup. Try again !!")
        break
    elif car_choice == 2:
        while True:
            print("1. 2-Tyre\n2. 4-Tyre")
            tyre_choice = int(input("Enter your tyre choice: "))
            if tyre_choice == 1:
                import suv
                import two_tyres
                break
            elif tyre_choice == 2:
                import suv
                import four_tyres
                break
            else:
                print("You can only select 2 or 4 tyre setup. Try again !!")
        break
    else:
        print("Please selece valid car !!")
        