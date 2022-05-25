from commonfunctions import factor

def problem3(x):
  factors = list(factor(x, True))
  print(f"Largest Prime Factor: {max(factors)}")

problem3(600851475143)