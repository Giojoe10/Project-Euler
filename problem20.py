from commonfunctions import fatorial

def problem20():
  target=100
  dSum = sum([int(n) for n in str(fatorial(target))])
  print(f"The sum of the digits in the number {target}! is {dSum}")

problem20()