import random

def game() :
    print ("Welcome to the Number Guessing Game!")
    score =random.randint(1,62)
    # Fetch The Hiscore 
    with open("D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != "") :
            hiscore = int(hiscore)
        else :
            hiscore = 0


    print(f"Your Score is : {score}")
    if(score > hiscore ):
        # write this hiscore to a file
        with open("hiscore.txt" , "w") as f:

            f.write(str(score))
    return score 

game()


# In This Game We Generate A Random Score For The Player And Compare It With The Hiscore Stored In A File. If The Player's Score Is Greater Than The Hiscore, We Update The Hiscore In The File.

# AGAR ("hiscore.txt") ye lgane se error aata hai to iska simple solution hai ki aap jis file me code likh rhe ho waha se is file ka path copy krke usme paste krdo. Jaise ki agar aapka code 
# "D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\02_PROBLEM.py" me hai 
# to aap "D:\MY FILES\S H I V A N S H U\CODING\VS COURSE FOLDERS\PYTHON COURSE\CHAPTER 9 -PS\hiscore.txt" ka path copy krke usme paste krdo. Isse aapko error nahi aayega.