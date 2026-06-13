#Check Number Entered By User Is Prime Or Not Using For Loop
a = int(input("Enter Your Number: "))

for i in range(2,a):
    if(a%i) == 0 :
     print("Number Is Not Prime")
     break
else:
   print("Number Is Prime")