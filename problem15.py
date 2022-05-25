from commonfunctions import combination

def problem15(grid):
  print(f"There are {int(combination(grid*2,grid))} routes in a {grid}x{grid} grid.")

problem15(20)