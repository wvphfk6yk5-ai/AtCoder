n = input()
cnt=0

if len(n)<4:
  print(int(n))

else:
  print(int(n[0:3]+"0"*(len(n)-3)))