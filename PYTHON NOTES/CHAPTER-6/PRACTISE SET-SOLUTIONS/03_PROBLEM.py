p1 = "Make A Lot Of Money"
p2 = "buy now"
p3 = "Subscribe This"
p4 = "Click This"

message = input("Enter Your Comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This Comment Is Spam")

else:
    print("This Comment Is Not Spam")

