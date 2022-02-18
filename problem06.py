def problem6():
  SQRoSUM= sum(range(100+1))**2
  SUMoSQR=0
  for x in range(100+1):
    SUMoSQR+=x**2

  print(f"The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {SQRoSUM-SUMoSQR}")

problem6()