a1 = int(input("Enter Your 1st No : "))
a2 = int(input("Enter Your 2nd No : "))
a3 = int(input("Enter Your 3rd No : "))
a4 = int(input("Enter Your 4th No : "))

if(a1>a2 and a1>a3 and a1>a4):
    print ("Greatest Number is a1:" , a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print ("Greatest Number is a2:" , a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print ("Greatest Number is a3:" , a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print ("Greatest Number is a4:" , a4)

else:
    print("No Any NUmber Is Greatest")