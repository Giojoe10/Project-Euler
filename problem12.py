from commonfunctions import factor

def problem12():
  x=1
  t=0
  while True:
    t += x
    if not isPrime(t):
      divisors = len(list(factor(t)))
      if divisors>=500:
        print(f"{t} is the first number to have over 500 divisors.")
        return
    x+=1

problem12()