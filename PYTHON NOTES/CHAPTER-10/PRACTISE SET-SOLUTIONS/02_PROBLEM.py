class calculator :
    def __init__(self , num):
        self.number = num
    
    def square(self):
        print(f"The Square Of {self.number} Is {self.number ** 2}")
    
    def cube(self):
        print(f"The Cube Of {self.number} Is {self.number ** 3}")
    
    def squareroot(self):
        print(f"The Square Root Of {self.number} Is {self.number ** 0.5}")

a = calculator(4)
a.square()
a.cube()
a.squareroot()
