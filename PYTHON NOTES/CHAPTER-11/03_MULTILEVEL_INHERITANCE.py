class employee :
    a = 1 

class programmer(employee) :
    b = 2

class manager(programmer) :
    c = 3 

o = employee()
print(o.a) # Prints The Attribute 
# print(o.b) # Throws An Error As The Object Of Employee Class Cannot Access The Attributes Of Programmer Class

o = programmer()
print(o.a , o.b) # Prints The Attribute As Programmer Class Inherits Employee Class
# print(o.c) # Throws An Error As The Object Of Programmer Class Cannot Access The Attributes Of Manager Class

o = manager()
print(o.a , o.b , o.c) # Prints The Attribute As Manager Class Inherits Programmer Class Which In Turn Inherits Employee Class
