words = ["Donkey" , "bad" , "gande" , "ganda"]

with open("CHAPTER 9 -PS/file.txt", "r") as f:
    content = f.read()

    for w in words:
        content = content.replace(w, "#"*len(w))

with open("CHAPTER 9 -PS/file.txt", "w") as f:
    f.write(content)