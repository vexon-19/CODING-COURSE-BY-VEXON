f = open("file.txt")

# readlines() method reads the entire file and returns a list of lines in the file. Each line is represented as a string in the list, including the newline character at the end of each line.

lines = f.readlines()
print(lines , type(lines))

# When you call readlines() multiple times, it will return an empty list after the first call because the file pointer is already at the end of the file.
#  To read the file again, you would need to reset the file pointer to the beginning of the file using f.seek(0) before calling readlines() again.

line1 = f.readlines()
print(line1 , type(line1))

line2 = f.readlines()
print(line2 , type(line2))

line3 = f.readlines()
print(line3 , type(line3))

line4 = f.readlines()
print(line4 , type(line4))

line5 = f.readlines()
print(line5 , type(line5))

# The Readline for while loop is used to read a file line by line. It reads one line at a time and processes it until the end of the file is reached.

line = f.readline()
while( line != ""):
    print(line )
    line = f.readline()

f.close()


