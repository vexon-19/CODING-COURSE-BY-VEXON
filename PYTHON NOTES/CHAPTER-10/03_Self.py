class employee:
  language = "Python"
  salary = 100000

  def getInfo(self):
     print(f"The Language Is {self.language} And The Salary Is {self.salary}")

  def greet(self):
     print("Hello Everyone")

  @staticmethod
  def greet():
      print("Hello Everyone")

harry = employee()
harry.language = "JavaScript" #This Is An Instance Attribute
 

harry.getInfo() # This Will Give An Error As We Have Not Passed The Object To The Method As We Are Calling The Method Using The Object.
employee.getInfo(harry) #This Is Another Way To Call The Method

harry.greet() # This Will Give An Error As We Have Not Passed The Object To The Method As We Are Calling The Method Using The Object.
# employee.greet(harry) #This Is Another Way To Call The Method