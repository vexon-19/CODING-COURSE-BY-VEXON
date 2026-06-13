class employee:
  language = "Python"
  salary = 100000

  def __init__(self , name , salary , language): #Dunder Method Which Is automatically called when we create an object of the class.
     self.name = name
     self.salary = salary
     self.language = language
     print("I Am Creating An Object")

  def getInfo(self):
     print(f"The Language Is {self.language} And The Salary Is {self.salary}")

  @staticmethod
  def greet():
      print("Hello Everyone")

harry = employee("Harry", 100000, "Python")
# harry.name = "Harry"
print(harry.name , harry.salary , harry.language)