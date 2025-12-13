h,w=map(int,input().split())
grid=[input().strip() for _ in range(h)]
mn=min(h,w)#max_n
n=0
s=[0]*(mn+1)
d=1

#バツの長さはdかどうか
def jadge_cross(y,x,d):
  shift=[[d,d],[d,-d],[-d,d],[-d,-d]]
  for dy,dx in shift:
    ny=y+dy
    nx=x+dx
    if not(0<=nx<w and 0<=ny<h):
      return False
    if grid[ny][nx] == ".":
      return False
  return True

#どんくらいdを伸ばせるか
def dfs(y,x,d):
  if not(jadge_cross(y,x,d)):
    return d-1
  else:
    return dfs(y,x,d+1)

#全探索((0,x)と(y,0)は中心となり得ないので除外)
for y in range(1,h):
  for x in range(1,w):
    if grid[y][x] == ".":
      continue
    n=dfs(y,x,d)
    if n>0:
      s[n]+=1

print(*s[1:mn+1])
  
