h,w = map(int,input().split())
grid = [input().strip() for _ in range(h)]
abcd =[]

for i,x in enumerate(grid):
  if x =="."*w:
    continue
  else:
    abcd.append([i,x])

ans=False

for i in range(w):
  for j in range(len(abcd)-1):
    if abcd[j][1][i] == abcd[j+1][1][i] == ".":
      break
    
    elif abcd[j][1][i] == abcd[j+1][1][i] ==  "#":
      continue
    
    elif abcd[j][1][i] == ".":
      print(abcd[j][0]+1,i+1)
      ans=True
      break
    
    else:
      print(abcd[j][0]+2,i+1)
      ans=True
      break
  if ans:
    break
