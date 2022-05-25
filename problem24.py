from commonfunctions import all_perms

def problem24():
  permutations = list(all_perms([0,1,2,3,4,5,6,7,8,9]))
  permutations = sorted(permutations)
  millionth = "".join([str(x) for x in permutations[999999]])
  print(f"The millionth lexicographic permutation is {millionth}")

problem24()