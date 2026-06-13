# d ={} #empty dictionary


marks = { "bittu" : 34,
        "shivanshu" : 45,
        "rahul" : 23,
        "sachin" : 67,
        "rohit" : 89 }

print(marks.items())  # prints all key-value pairs as a list of tuples

print(marks.keys())  # prints all the keys in the dictionary

print(marks.values())  # prints all the values in the dictionary

marks.update({"bittu": 90 , "ankit" : 76})  # updates bittu's marks to 90 & adds ankit with marks 76
print(marks)  # prints the updated dictionary

print(marks.get("shivanshu"))  # prints the marks of shivanshu using get() method
print(marks["shivanshu"])  # prints the marks of shivanshu using direct access

print(marks.get ("non_existent_key"))  # prints None since the key doesn't exist
# print(marks["non_existent_key"])  # This will raise a KeyError since the key doesn't exist

print(marks.pop("rohit"))  # removes rohit from the dictionary and prints his marks
print(marks)  # prints the dictionary after removing rohit

marks.clear()  # clears the entire dictionary
print(marks)  # prints the empty dictionary

marks = { "bittu" : 34,
        "shivanshu" : 45,   
        "rahul" : 23,
        "sachin" : 67,
        "rohit" : 89 }
copied_marks = marks.copy()  # creates a shallow copy of the dictionary
print(copied_marks)  # prints the copied dictionary

print(len(marks))  # prints the number of key-value pairs in the dictionary
print(marks.setdefault("new_student", 50))  # adds new_student with marks 50 and prints the value
print(marks)  # prints the dictionary after adding new_student
print(marks.setdefault("bittu", 100))  # prints bittu's marks without changing it
print(marks)  # prints the dictionary to show bittu's marks remain unchanged
print(marks.popitem())  # removes and prints an arbitrary key-value pair from the dictionary
print(marks)  # prints the dictionary after popping an item

del marks["sachin"]  # deletes the entry for sachin
print(marks)  # prints the dictionary after deleting sachin

# Note: The order of items in the dictionary may vary when using popitem() as it removes an arbitrary item.

#--------------------------------------------x------------------------------------------------------------------