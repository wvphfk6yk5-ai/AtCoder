n,m,h,k = map(int,input().split())
s = input().strip()
grid=set(tuple(map(int,input().split())) for _ in range(m))
r=[0,0]
cnt=0

shift={"R":(1,0),"L":(-1,0),"D":(0,-1),"U":(0,1)}

for ds in s:

  h-=1
  cnt+=1
  if h < 0:
    print("No")
    exit()
  
  if h-(n-cnt) >= 0:
    print("Yes")
    exit()
  
  
  r[0] += shift[ds][0]
  r[1] += shift[ds][1]
  
  if h < k:
    nr=(r[0],r[1])
    if nr in grid:
      h = k
      grid.remove(nr)

    
  
  
  
  
  
  
  
