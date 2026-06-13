
with open ("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines :
    if("Python" in line):
        print(f"Python is present in the file. Line no: {lineno}")
        break 
    lineno += 1
else:
    print("Python is not present in the file")


