t=int(input())

ns=[]
grids=[]
for i in range(t):
  n = int(input())
  grid = [list(map(int,input().split())) for _ in range(n)]
  ns.append(n)
  grids.append(grid)

def count(n,grid):
  w=sum(y for y,x in grid)
  p=0
  x = sorted(range(n), key=lambda i : (grid [i][1] + grid[i][0])*-1)
  cnt=n

  for i in x:
    
    p += grid[i][1]
    w -= grid[i][0]
    cnt-=1
    
    if p >= w:
      break

  if w == 0:
    cnt = 0

  return cnt
  
for i in range(t):
  print(count(ns[i],grids[i]))