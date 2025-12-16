n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(m)]
cnt=0

for i in range(1,n+1):
  nei = set()
  for j in range(m):
    for k in range(n):
      if grid[j][k] == i:
        if 0<= k-1:
          nei.add(grid[j][k-1])
        if k+1 < n:
          nei.add(grid[j][k+1])
  cnt += n-1-len(nei)


print(cnt//2)