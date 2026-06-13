a = int(input("enter your age: "))


# IF 'ELIF' , 'ELSE ' LADDER 
if(a>=18):
    print("you Are Above The age of consent ")
    print("Good For You")


elif(a<0):
    print("You Are Entering Invalid Age")


elif(a==0):
    print("You Are Entering 0 Which Is Not a Valid Age")


else:
    print("You Are Below The Age Of Consent") 