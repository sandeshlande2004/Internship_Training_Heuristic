class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def result(self):
        print(f"Addition of {self.a} and {self.b} is {self.a + self.b}")
    
    
class sub:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def result(self):
        print(f"Subtraction of {self.a} and {self.b} is {self.a - self.b}")

class mul:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def result(self):
        print(f"Multiplication of {self.a} and {self.b} is {self.a * self.b}")

class div:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def result(self):
        print(f"Division of {self.a} and {self.b} is {self.a / self.b}")

obj_1 = add(10,20)
obj_2 = sub(20,10)
obj_3 = mul(15,2)
obj_4 = div(100,5)

#Either we can call result one by one
obj_1.result()
obj_2.result()
obj_3.result()
obj_4.result()

#---------------------------OR--------------------------------------#

#we can use for loop to call all at once

for a in (obj_1,obj_2,obj_3,obj_4):
    a.result()
    
    