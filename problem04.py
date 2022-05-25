def problem4():
  g = 0
  mult=[0,0]
  for x in range(999,100,-1):
    for y in range(999,100,-1):
      result = str(x*y)
      #print(result)
      if int(g)<(x*y):
        if result == result[::-1]:
          g=result
          mult[0] = x
          mult[1] = y

      y-=1
    y=999
    x-=1
  print(f"The largest palindrome for the product of two {len(str(x))}-digit numbers is {g} ({mult[0]} x {mult[1]})")

problem4()