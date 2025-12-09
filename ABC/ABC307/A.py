N=int(input())
A=list(map(int,input().split()))
result=[]

for i in range(N):
  sum=0
  for j in range(7):
    sum+=A[j+7*i]
  result.append(sum)

print(*result)

  
