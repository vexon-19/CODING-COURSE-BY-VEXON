friends = ["Shivanshu", "Ankit", 6, 345.5, "Ajay" , False , "Ankur"]
print(friends)

friends.append("Rohit")  # adds "Rohit" at the end of the list
print(friends)

friends.remove("Ankit")  # removes "Ankit" from the list
print(friends)

friends.pop()  # removes the last element from the list
print(friends)

friends.insert(1, "Ankit")  # inserts "Ankit" at index 1
print(friends)

friends.sort(key=str)  # sorts the list (only works if all elements are of the same type)
print(friends)

print(friends.index("Ajay"))  # prints the index of "Ajay"

print(friends.count("Bittu"))  # counts how many times "Bittu" appears in the list


friends.reverse()  # reverses the list
print(friends)

length = len(friends)  # gets the length of the list
print(length)

#---------------------------------------IGNORE------------------------------------------------------------
