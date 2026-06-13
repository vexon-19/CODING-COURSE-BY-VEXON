f = open("myfile.txt")
print(f.read())
f.close()

# The Same Can Be Written Using With Statement

with open("myfile.txt") as f:
    print(f.read())

# You Dont Have To Explicityly Close The File When You Use With Statement 
# It Automatically Closes The File After The Block Of Code Is Executed.