from commonfunctions import fatorial
def problem34():
  upperLimit=6*(fatorial(9))
  results=[]
  l =[sum([fatorial(digit) for digit in [int(d) for d in str(x)]]) for x in range(3,upperLimit)]
  for i,sumDigits in enumerate(l):
    if i+3==sumDigits:
      results.append(i+3)
  print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is {sum(results)}")

problem34()