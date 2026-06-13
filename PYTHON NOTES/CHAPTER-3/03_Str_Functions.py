name = "BITTU"
name1 = "bittu"
name2 = " bittu gaming"

print(len(name))  # Output: 5

print(name.endswith("U"))  # Output: True

print(name.startswith("Bi"))  # Output: false

print(name.startswith("B"))  # Output: true

print(name.count("T"))  # Output: 2

print(name1.capitalize())  # Output: Bittu

print(name2.title())  # Output:  Bittu Gaming

print(name2.upper())  # Output:  BITTU GAMING

print(name2.lower())  # Output:  bittu gaming

print(name2.strip())  # Output: bittu gaming

print(name2.replace("bittu", "BITTU"))  # Output:  BITTU gaming

print(name.split("i"))  # Output: ['b', 'ttu']

print(name.find("T"))  # Output: 2

print(name.index("T"))  # Output: 2

#---- Additional String Functions --#
print(name.isalnum())  # Output: True
print(name.isalpha())  # Output: True
print(name.islower())  # Output: False
print(name.isupper())  # Output: True
print(name.isspace())  # Output: False
print(name.swapcase())  # Output: bittu
print(name.center(10, '*'))  # Output: **BITTU***

# ----------------------------------------- IGNORE------------------------------------------- ---