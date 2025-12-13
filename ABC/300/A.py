n,a,b=map(int,input().split())
c=[-1]+list(map(int,input().split()))
ans=a+b

for i in range(1,n+1):
  if ans == c[i]:
    print(i)
    break

  
