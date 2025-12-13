h,w=map(int,input().split())
a=[input().strip() for _ in range(h)]
b=[input().strip() for _ in range(h)]
ans=False

def shift(a,dy,dx):
  res=[]
  for i in range(h):
    row=a[(i+dy)%h]
    row2=row[dx:]+row[:dx]
    res.append(row2)
  return res

for dy in range(h):
  for dx in range(w):
    if shift(a,dy,dx) == b:
      ans = True
      break
  if ans:
    break

print("Yes" if ans else "No")
    
