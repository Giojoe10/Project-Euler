def problem9():
  rng = 1000
  for a in range(rng):
    b=a
    for b in range(rng):
      c=b
      for c in range(rng):
        if a<b<c and (a**2)+(b**2)==(c**2) and a+b+c==1000:
          print(f"{a}² + {b}² = {c}² => {a**2} + {b**2} = {c**2} and {a}+{b}+{c}=1000, and their product is {a*b*c}")
          return
          

problem9()