from commonfunctions import numberToWords

def problem17():
  sum = 0
  for x in range(1,1000+1):
    sum+=len(numberToWords(x))
  print(sum)

problem17()
