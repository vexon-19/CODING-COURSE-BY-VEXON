import os

path = "D:/MY FILES/"  # change this to your directory path
contents = os.listdir(path)
for item in contents:
    print(item)
