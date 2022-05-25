def problem16():
  power = 1000
  l = [int(x) for x in [n for n in str(2**power)]]
  print(f"The sum is {sum(l)}")

problem16()