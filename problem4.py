def problem4():
  x=999
  y=999
  while x>=100:
    while y>=100:
      result = str(x*y)
      if result == result[::-1]:
        print(f"The largest palindrome for the product of two {len(str(x))}-digit numbers is {result} ({x} x {y})")
        return
      y-=1
    y=999
    x-=1

problem4()