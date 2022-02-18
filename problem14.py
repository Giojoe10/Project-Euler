from commonfunctions import conjecture

def problem14():
  max=[0,0]
  l=0
  for x in range(1,1000000):
    l = len(conjecture(x))
    if l>max[1]:
      max = [x, l]  
  print(f"The starting number that produces the lognest chain ({max[1]}) is {max[0]}")

problem14()