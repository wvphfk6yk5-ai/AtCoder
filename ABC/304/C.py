from collections import deque

n,d = map(int,input().split())
grid = [None]+[list(map(int,input().split())) for _ in range(n)]
inf = [False,True]+[False]*(n-1)
new = deque()
new.append(1)

while new:
  x = new.popleft()
  for i in range(1,n+1):
    r = (grid[x][0]-grid[i][0])**2+(grid[x][1]-grid[i][1])**2
    #print(r > d**2)
    if inf[i] or r > d**2:
      continue
    
    else:
      inf[i] = True
      new.append(i)
#print(inf)

for i in range(1,n+1):
  print("Yes" if inf[i] else "No")
  