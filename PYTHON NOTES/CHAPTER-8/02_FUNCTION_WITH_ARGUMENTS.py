def GoodDay(name):
    print("Good Day" + name)
GoodDay("Bittu")

def GoodDay(name , ending):
    print("Good Day" + name)
    print(ending)
GoodDay("Bittu" , " Thanks")


def GoodDay(name , ending):
    print("Good Day" + name)
    print(ending)
    return "done"

a = GoodDay("Bittu" , " Thanks")
print(a)