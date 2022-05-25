def problem36():
  palindromics10 = [x for x in range(1_000_000) if str(x)==str(x)[::-1]]
  results = {x:str(bin(x))[2:] for x in palindromics10 if str(bin(x))[2:]==str(bin(x))[2:][::-1]}
  finalResult = sum(results.keys())
  print(finalResult)

problem36()