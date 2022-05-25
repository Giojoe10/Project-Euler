def problem48():
  powers = [x**x for x in range(1000+1)]
  result = sum(powers)-1
  print(f"The last ten digits of the series are {str(result)[-10:]}")

problem48()