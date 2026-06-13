marks = { "bittu" : 34,
        "shivanshu" : 45,
        "rahul" : 23,
        "sachin" : 67,
        "rohit" : 89 }

print(marks , type(marks))  # prints the type of marks which is dictionary

print(marks["bittu"])  # prints the marks of bittu


marks["bittu"] = 78  # updates the marks of bittu to 78
print(marks)  # prints the updated dictionary


marks["ankit"] = 56  # adds a new entry for ankit with marks 56
print(marks)  # prints the dictionary with the new entry


del marks["rahul"]  # deletes the entry for rahul
print(marks)  # prints the dictionary after deleting rahul

