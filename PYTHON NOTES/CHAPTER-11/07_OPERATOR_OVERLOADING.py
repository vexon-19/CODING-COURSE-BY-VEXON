class Number :
  def __init__(self , n ):
     self.n = n

  def __add__(self , num):
    return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m) # Throws An Error As The Interpreter Does Not Know How To Add Two Objects Of The Class Number