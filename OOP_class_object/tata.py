# class tata:
#     def __init__(self,EV,CNG,Diesel):
#         self.EV = EV
#         self.CNG = CNG
#         self.Diesel = Diesel

# obj_1 = tata('Nexon','Tigor','Tiago')
# print(obj_1.EV)
# obj_2 = tata('Punch','Harrier','Safari')
# print(obj_2.CNG)
# obj_3 = tata('Indica','Indigo','Sumo')
# print(obj_3.Diesel)

class tata:
    def __init__(self,car_type,engine_type):
        self.car_type = car_type
        self.engine_type = engine_type
    
    def display(self):
        print(f"Car Type: {self.car_type} and Engine Type: {self.engine_type}")
    
obj_1 = tata
while True:
    print("1. Punch\n2. Harrier\n3. Safari")
    car_choice = int(input("Enter your choice: "))
    if car_choice > 3:
        print("Invalid choice")
        continue
    print("1. EV\n2. Diesel\n3. CNG")
    engine_choice = int(input("Enter your choice: "))
    if car_choice == 1 and engine_choice == 1:
        obj_1 = tata('Punch','EV')
        obj_1.display()
        break
    elif car_choice == 1 and engine_choice == 2:
        obj_1 = tata('Punch','Diesel')
        obj_1.display()
        break
    elif car_choice == 1 and engine_choice == 3:
        obj_1 = tata('Punch','CNG')
        obj_1.display()
        break
    elif car_choice == 2 and engine_choice == 1:
        obj_1 = tata('Harrier','EV')
        obj_1.display()
        break
    elif car_choice == 2 and engine_choice == 2:
        obj_1 = tata('Harrier','Diesel')
        obj_1.display()
        break
    elif car_choice == 2 and engine_choice == 3:
        obj_1 = tata('Harrier','CNG')
        obj_1.display()
        break
    elif car_choice == 3 and engine_choice == 1:
        obj_1 = tata('Safari','EV')
        obj_1.display()
        break
    elif car_choice == 3 and engine_choice == 2:
        obj_1 = tata('Safari','Diesel')
        obj_1.display()
        break
    elif car_choice == 3 and engine_choice == 3:
        obj_1 = tata('Safari','CNG')
        obj_1.display()
        break
    else:
        print("Invalid choice")
    
    
    


