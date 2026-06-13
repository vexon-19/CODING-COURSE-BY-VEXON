class demo :
    a = 4 

o = demo()
print(o.a) # We Can Access The Class Attribute Using The Object Of The Class.

o.a = 0
print(o.a) # This Will Print 0 As We Have Created An Instance Attribute With The Same Name As The Class Attribute.
print(demo.a) # This Will Print 4 As We Are Accessing The Class Attribute Using The Class Name.