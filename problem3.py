def problem3(x):
  prime = 0
  for i in range(2,int(x/2)):
    if x%i==0:
      x=x/i
      if i>prime:
        prime = i
      i-=1
      if i>=int(x/2):
        break

  print(f"Largest Prime Factor: {int(prime)}")


problem3(600851475143)