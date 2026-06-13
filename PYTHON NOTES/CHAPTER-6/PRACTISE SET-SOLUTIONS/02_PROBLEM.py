marks1 = int(input("Enter Marks 1:"))
marks2 = int(input("Enter Marks 2:"))
marks3 = int(input("Enter Marks 3:"))

#Check For Total %ge

total_percentage = (100*(marks1 + marks2 + marks3)/300)

if(total_percentage>=40):
    print("YOU ARE PASS" , total_percentage)

else: 
    print("You Fail Try Again Next Year ! ", total_percentage )