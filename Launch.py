import os
numLen = int(input("How many digits of pi will you calculate? "))
numLen = 10**numLen
sys.stdout=open("RAM.txt","a")
print(numLen)
sys.stdout.close()
call([launch.bat])
os.remove(RAM.txt)
os.remove(NRAM.txt)
f = open("pi.txt")
lines = f.readlines()
for line in lines:
    print line
