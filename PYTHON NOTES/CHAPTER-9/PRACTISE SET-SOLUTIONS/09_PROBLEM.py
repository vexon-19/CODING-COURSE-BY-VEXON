with open ("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS \ file.txt") as f :
    content1 = f.read()

with open ("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Both the files are same")
else:
    print("Both the files are different")