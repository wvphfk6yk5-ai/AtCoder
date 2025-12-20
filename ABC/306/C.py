n = int(input())
a = list(map(int,input().split()))
b =set()
ans=[]
t=[False]*(n+1)

for x in a:
  if t[x]:
    continue
  
  elif x in b :
    ans.append(x)
    t[x] = True
  else:
    b.add(x)

print(*ans)
