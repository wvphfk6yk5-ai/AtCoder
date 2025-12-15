n,m = map(int,input().split())
s = [input().strip() for _ in range(n)]

def diff(a,b):
  c=0
  for i in range(m):
    if a[i] != b[i]:
      c+=1
  return True if c==1 else False

def yesorno(i,cnt,used):
  used[i] = True
  if cnt == n:
    return True
  
  for j in range(n):
    if used[j]:
      continue
    
    if diff(s[i],s[j]):
      if yesorno(j,cnt+1,used):
        return True
  
  used[i] = False 
  return False

for i in range(n):
  used = [False]*n
  if yesorno(i,1,used):
    print("Yes")
    exit()

print("No")