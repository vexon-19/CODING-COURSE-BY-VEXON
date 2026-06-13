class employee:
  language = "Python"
  salary = 100000


harry = employee()
harry.name = "Harry" #This Is An Instance Attribute
print(harry.name , harry.language , harry.salary) 

rohan = employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name , rohan.language , rohan.salary)

# Here name is an instance attribute and language and salary are class attributes as they directly belong to the
#class and are shared by all the objects of the class.