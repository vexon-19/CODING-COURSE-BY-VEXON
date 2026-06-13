def rem(l , word):
    
    for item in l :
        l.remove(word)
        return l 

l = ["Bittu" , "Rohan" , "Shubham" , "an"]

print(rem(l , "an"))


#Another Way
def rem(l , word):
    n = []
    for item in l :
        if not (item ==word):
            n.append(item.strip(word))
    return n 

l = ["Bittu" , "Rohan" , "Shubham" , "an"]
print(rem(l , "an"))