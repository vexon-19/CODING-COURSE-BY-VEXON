class employee :
    company = "Google"
    def show (self):
        print (f"The Name Of The Employee is {self.name} and the salary is {self.salary}")

# -------------------------------NORMAL WAY OF CREATING OBJECTS-------------------------------

# class programmer :
#     company = "Microsoft"
#     def show (self):
#         print (f"The Name is {self.name} and the salary is {self.salary}")

#     def showlanguage (self):
#         print (f"The Name Is  {self.name} and he is good with {self.language} language ")

    
# -------------------------------CREATING OBJECTS USING INHERITANCE-------------------------------
class programmer(employee) :
    company = "Microsoft"
    def showlanguage (self):
        print (f"The Name Is  {self.name} and he is good with {self.language} language ")

a = employee()
b = programmer()

print(a.company , b.company)