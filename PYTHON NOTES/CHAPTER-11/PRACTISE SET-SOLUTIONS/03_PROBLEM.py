class Employee :
    salary = 234
    increment = 20

    @property
    def salaryafterincrement (self):
      return (self.salary + self.increment * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement (self , salary):
        self._increment = ((salary/self.salary)-1)*100

e = Employee()

e.salaryafterincrement = 280.8
print(e._increment)
