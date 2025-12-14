n = int(input())
a = list(map(int,input().split()))
Max=len(a)-1
Min=0

def arr(a,Max,Min):
  for i in range(Min,Max):
    if abs(a[i]-a[i+1]) == 1:
      continue
    
    if a[i] < a[i+1]:
      add = []
      for da in range(a[i]+1,a[i+1]):
        add.append(da)
      na = a[:i+1]+add+a[i+1:]
      Max=len(na)-1
      Min=i+a[i+1]-a[i]-1
      return arr(na,Max,Min)
    
    if a[i] > a[i+1]:
      add = []
      for da in range(a[i]-1,a[i+1],-1):
        add.append(da)
      na = a[:i+1]+add+a[i+1:]
      Max=len(na)-1
      Min=i-a[i+1]+a[i]-1
      return arr(na,Max,Min)
  
  return a

print(*arr(a,Max,Min))