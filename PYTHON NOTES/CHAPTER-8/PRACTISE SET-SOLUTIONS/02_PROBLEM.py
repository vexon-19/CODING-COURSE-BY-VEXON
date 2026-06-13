#Convert Tempreture Farenheit To Celcius Using Python 

#First Way
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter Tempreture In F : "))
print(f_to_c(f))

#Second Way
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter Tempreture In F : "))
c = f_to_c(f)
print(f"{round(c,2)} C ")