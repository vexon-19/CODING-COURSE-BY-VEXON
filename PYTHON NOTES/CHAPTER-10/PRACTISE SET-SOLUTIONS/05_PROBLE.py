from random import randint 
class train :
    def book (self , trainNo , fro , to):
        print (f"Ticket is booked in train no : {trainNo} from{fro} to {to}")

    def getstatus(self , trainNo):
        print(f"Train no : {trainNo} is running on time")

    def getfare(self , trainNo , fro , to  ):
        print(f"Ticket fare in train no : {trainNo} from {fro} to {to} is {randint(222 , 5555)}")

t = train()
t.book(12186 , "Rewa" , "RKMP")
t.getstatus(12186)
t.getfare(12186 , "Rewa" , "RKMP")