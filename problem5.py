def problem5():
  n=1
  divisible = True
  while True:
    divisible = True
    for x in range(1,20):
      if n%x!=0:
        divisible = False
        break
    if divisible ==  True:
      print(f"The smallest positive number that can be evenly divisible by all of the number from 1 to 20 is: {n}")
      return
    n+=1

problem5()