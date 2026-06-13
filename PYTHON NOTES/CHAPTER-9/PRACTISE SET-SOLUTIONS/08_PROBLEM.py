with open("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\ this.txt") as f:
    content = f.read()

with open ("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\ this_copy.txt", "w") as f:
    f.write(content)