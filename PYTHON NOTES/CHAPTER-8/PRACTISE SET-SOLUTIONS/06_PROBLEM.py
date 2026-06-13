#Convert Inces To Centimetre Using Python

def inch_to_cms(inch):
    return inch*2.54

n = int(input("Enter Value In Inces: "))

print(f"The Corresponding Value In Cms Is {inch_to_cms(n)}")