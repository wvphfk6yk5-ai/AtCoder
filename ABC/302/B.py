h,w = map(int,input().split())
s = [input().strip() for _ in range(h)]
a = "snuke"


for i in range(h):
  for j in range(w):
    if j+4 < w:
      if all(s[i][j+n] == a[n] for n in range(5)):
        for n in range(5):
          print(i+1,j+n+1)
        exit()
    if j-4 >=0:
      if all(s[i][j-n] == a[n] for n in range(5)):
        for n in range(5):
          print(i+1,j-n+1)
        exit()

      
for j in range (w):
  for i in range(h):
    if i+4 < h:
      if all(s[i+n][j] == a[n] for n in range(5)):
        for n in range(5):
          print(i+n+1,j+1)
        exit()
    if i-4 > 0:
      if all(s[i-n][j] == a[n] for n in range(5)):
        for n in range(5):
          print(i-n+1,j+1)
        exit()


for i in range(h):
  for j in range(w):
    if i+4 < h and j+4 <w:
      if all(s[i+n][j+n] == a[n] for n in range(5)):
        for n in range(5):
          print(i+n+1,j+n+1)
        exit()
    if i+4 < h and j-4 >=0:
      if all(s[i+n][j-n] == a[n] for n in range(5)):
        for n in range(5):
          print(i+n+1,j-n+1)
        exit()
    if i-4 >=0 and j+4 <w:
      if all(s[i-n][j+n] == a[n] for n in range(5)):
        for n in range(5):
          print(i-n+1,j+n+1)
        exit()
    if i-4 >=0 and j-4 >=0:
      if all(s[i-n][j-n] == a[n] for n in range(5)):
        for n in range(5):
          print(i-n+1,j-n+1)
        exit()

    


    