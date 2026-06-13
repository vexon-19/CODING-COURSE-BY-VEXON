# ---------------------------------------BY CHATGPT------------------------------------------
class Programmer:
    company = "Microsoft"   # class attribute (same for all)

    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience  # in years

    def get_info(self):
        return f"Name: {self.name}\nCompany: {self.company}\nLanguage: {self.language}\nExperience: {self.experience} years\n"


# Creating objects (programmers)
p1 = Programmer("Aman", "Python", 3)
p2 = Programmer("Riya", "Python", 5)
p3 = Programmer("Karan", "Python", 2)

# Sharing/displaying information
print(p1.get_info())
print(p2.get_info())
print(p3.get_info())

# ---------------------------------------BY CODE WITH HARRY---------------------------------------
class programmer :

 company ="Microsoft"
 def __init__(self , name , salary , pin):
    self.name = name 
    self.salary = salary
    self.pin = pin

p = programmer ("Harry", 100000, 123456)
print(p.name , p.salary , p.pin )
r = programmer ("Rohan", 200000, 654321)
print(r.name , r.salary , r.pin )


