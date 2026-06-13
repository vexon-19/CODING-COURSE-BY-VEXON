class employee :
    company = "Google"
    name = "Default name "
    salary = 125780
    def show (self):
        print (f"The Name Of The Employee is {self.name} and the salary is {self.salary}")

class coder : 
    language = "Python"
    def printlanguages(self):
        print (f"Out Of All The Languages Here Is Your Language : {self.language}")





class programmer(employee , coder ) :
    company = "Microsoft"
    def showlanguage (self):
        print (f"The Name Is  {self.company} and he is good with {self.language} language ")

a = employee()
b = programmer()

b.show()
b.printlanguages()
b.showlanguage()

