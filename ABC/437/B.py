h,w,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = [int(input()) for _ in range(n)]
ans = [0]*h

for i in range(h):
  for j in range(w):
    for k in range(n):
      if b[k] == a[i][j]:
        ans[i]+=1
  

print(max(ans))