word = "Donkey"

with open("CHAPTER 9 -PS/file.txt", "r") as f:
    content = f.read()

    new_content = content.replace(word, "#####")
with open("CHAPTER 9 -PS/file.txt", "w") as f:
    f.write(new_content)