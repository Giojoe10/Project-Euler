def downloadFile(url):
  import requests
  r = requests.get(url, allow_redirects=True)
  with open("p022_names.txt","wb") as f:
    f.write(r.content)

def problem22():
  with open("p022_names.txt", "r+") as f:
    for line in f:
      names=line.replace('"',"").replace(","," ")
  names = names.split(" ")
  names=sorted(names)
  values = [lettersum(x)*(names.index(x)+1) for x in names]
  print(sum(values))

#downloadFile("https://projecteuler.net/project/resources/p022_names.txt")
problem22()
