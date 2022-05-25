from commonfunctions import sumProperDivisors

def problem21():
  sum=0
  for x in range(1,10000):
    n=sumProperDivisors(x)
    k=sumProperDivisors(n)
    if n!=k and k==x:
      sum+=x+k
  print(f"The sum of all amicable numbers under 10 000 is {int(sum/2)}")

problem21()