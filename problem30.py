def problem30():
  power = 5
  upperLimit=6*(9**power)
  results=[]
  l =[sum([digit**power for digit in [int(d) for d in str(x)]]) for x in range(2,upperLimit)]
  for i,sumDigits in enumerate(l):
    if i+2==sumDigits:
      results.append(i+2)
  print(f"The sum of all the numbers that can be written as the sum of fifth powers of their digits is {sum(results)}")

problem30()