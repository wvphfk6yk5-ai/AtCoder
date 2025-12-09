n=int(input())
s=[input().strip() for _ in range(n)]
marge=str()
ans=False

for i in range(n):
  for j in range(n):
    if i == j :
      continue
    marge=s[i]+s[j]

    if (marge == marge[::-1]):
      ans=True
      break
  
if ans:
  print("Yes")
else:
  print("No")
