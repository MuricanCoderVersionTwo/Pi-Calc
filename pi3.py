f = open("RAM.txt")
lines = f.readlines()
for line in lines:
    x = 9
  pi = 0
  while x <= piLen:
    pi = pi + (4/x)
    pi = pi - (4/(x+2))
    x = x + 16
  sys.stdout=open("pi.txt","a")
  print("The time difference is", (now1 - now).total_seconds(), "seconds")
  sys.stdout.close()
