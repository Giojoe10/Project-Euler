def problem29():
  Max = 100
  results=[]
  for a in range(2,Max+1):
    for b in range(2,Max+1):
      n = a**b
      if n not in results:
        results.append(n)

  print(f"There are {len(results)} distinct terms.")

problem29()