from commonfunctions import isPrime

def problem10():
  primes = [x for x in range(2,2000000) if isPrime(x)]
  print(f"The sum of the primes ({primes}) is {sum(primes)}")

problem10()