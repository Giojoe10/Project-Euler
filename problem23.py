from commonfunctions import perfectNumber

sums = [x for x in range(2,28123+1) if perfectNumber(x)=="Abundant"]

def problem23():
  result =[False]*28124
  for i in sums:
    for j in sums:
      s=i+j
      if s>28123:
        break
      result[s]=True
  final = sum([i for i,x in enumerate(result) if not x])
  print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers is:",final)

problem23()