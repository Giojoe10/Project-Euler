from commonfunctions import conjecture

def problem14():
  lengths=[len(list(conjecture(x))) for x in range(1,1_000_000)]
  print(f"The starting number that produces the longest chain ({max(lengths)}) is {lengths.index(max(lengths))+1}")

problem14()