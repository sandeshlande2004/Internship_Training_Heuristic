class parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def result(self):
        print(f"Addition of {self.a} and {self.b} is {self.a + self.b}")
        

class child(parent):
    pass

obj = child(15,20)
obj.result()