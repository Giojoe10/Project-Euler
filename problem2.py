def problem2():
  soma = 0
  current = 1
  previous1=1
  previous2=1
  while current<4000000:
    if current%2==0:
      soma+=current
    previous2, previous1 = previous1, current
    current = previous1+previous2
  print(soma)

problem2()