def problem25():
  i = 1
  current = 1
  previous1=1
  previous2=1
  while True:
    i+=1
    previous2, previous1 = previous1, current
    current = previous1+previous2
    if len(str(current))>=1000: 
      break
  print(f"The first term in the Fibonacci sequence to contain 1000 digitis is the {i+1} term.")

problem25()