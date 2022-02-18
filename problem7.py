from commonfunctions import isPrime

def problem7():
  wanted=10001
  y=[]
  x=2
  while True:
    if isPrime(x):
      y.append(x)
    if len(y)>=wanted:
      print(f"The {wanted} prime is {y[wanted-1]}")
      return
    x+=1
  

problem7()