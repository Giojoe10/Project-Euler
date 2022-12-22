def isPrime(x):
  """This function returns if the input is prime or not"""
  for i in range(2,int((x/2)+1)):
       if (x%i==0): return False
  return True


def generate_primes(length: int):
    """This function returns a list of [length] prime numbers"""
    primes = []
    i=2
    while len(primes)<length:
        if isPrime(i):
            primes.append(i)
        i=i+1
    return primes

def conjecture(x):
  """This function yields the Collatz conjecture of the input"""
  yield x
  while x != 1:
    if x%2==0:
      x = x/2
      yield int(x)
    else:
      x=3*x+1
      yield int(x)

def factor(x, Prime=False):
  """
  This function yields all the divisors of a number
  If the argument Prime is true, it will only yield
  the prime factors of that number
  """
  if not Prime:
    for i in range(1,int(m.sqrt(x))+1):
      if x%i==0:
        yield i
        if i**2!=x:
          yield x/i
  else:
    i=1
    while i<=int(m.sqrt(x)+1):
      if x%i==0:
        yield i
        x=x/i
      i+=1


"""Returns the sum of all positive integers before the input"""
triangleNumber = lambda x: int(x*(x+1)/2) if x>=1 else -1

"""Returns the product of all positive integers before the input"""
fatorial = lambda n: n*fatorial(n-1) if n>1 else 1
 
def combination(n,k):
  """This function returns the combination of the inputs"""
  return fatorial(n)/(fatorial(k)*fatorial(n-k))

"""Return the sum of all divisors of a number, except itself"""
sumProperDivisors = lambda n: sum(list(factor(n)))-n

def repetition(list):
  """Yield the elements that repeat in the list"""
  seen=[]
  for x in list:
    if x in seen:
      yield list.index(x)
    else:
      seen.append(x)

def all_perms(elements):
  """Yields all the permutations of the elements from the given list"""
  if len(elements) <=1:
    yield elements
  else:
    for perm in all_perms(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + perm[i:]


def numberToWords(n):
  """
  This function returns a string with the
  inputted number written out in English
  without spaces or hyphens.
  """
  basic = ["","one","two","three","four","five","six", "seven", "eight", "nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
  tens = ["","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
  words=""
  nstring=str(n)
  if len(nstring)>=4:
    words+=basic[int(nstring[-4])]+ "thousand"
  if len(nstring)>=3 and int(nstring[-3])>0:
    words+=basic[int(nstring[-3])]+ "hundred"
    if int(nstring[-2:])>0:
      words+="and"
  if int(nstring[-2:])>0:
    if int(nstring[-2:])>=20:
      
      words+=tens[int(nstring[-2])-1] + basic[int(nstring[-1])]
    elif int(nstring[-2:])>0:
      words+=basic[int(nstring[-2:])]
  return words


def lettersum(input):
  """
  This function returns the sum of the values
   of all letters in a string, where a=1, b=2 and so on.
  """
  import string
  dicio={b:a+1 for a,b in enumerate(string.ascii_uppercase)}
  sum = 0
  for letter in input:
    sum += dicio[letter]
  return sum
  

def perfectNumber(x):
  """This function returns what if a number is perfect,
  deficient or abundant
  """
  y = sumProperDivisors(x)
  if x==y:
    return "Perfect"
  elif x>y:
    return "Deficient"
  else:
    return "Abundant"
