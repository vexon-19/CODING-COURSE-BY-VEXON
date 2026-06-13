class employee :
    a = 1
    def show (self):
        print (f"The Class Value Of a is {self.a}")

e = employee()
e.a = 45

e.show()

# -------------------------------CLASS METHODS-------------------------------

class employee :
    a = 1
    @classmethod
    def show (cls):
        print (f"The Class Attribute Of a is {cls.a}")

e = employee()
e.a = 45
e.show()