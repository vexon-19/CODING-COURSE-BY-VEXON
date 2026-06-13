with open ("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\log.txt") as f:
    content = f.read()

if("Python" in content):
    print("Python is present in the file")
else:
    print("Python is not present in the file")


