#Factorial Using For Loop
a = int(input("Enter Your Number: ")) 

product = 1

for i in range(1 , a+1):
    product = product*i

print(f"The Factorial of {a} is {product}")