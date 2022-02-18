def isPrime(x):
  for i in range(2,int((x/2)+1)):
    if x%i==0:
      return False
  return True

def conjecture(entrada):
  y=[]
  y.append(entrada)
  i=0
  while entrada != 1:
    if (entrada % 2) == 0:
      entrada = entrada/2
      y.append(int(entrada))
    else:
      entrada = (entrada*3)+1
      y.append(int(entrada))

  return y