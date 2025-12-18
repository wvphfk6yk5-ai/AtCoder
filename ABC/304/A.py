n = int(input())
li = [list(input().split()) for _ in range(n)]
li2 =[0]*n

for i in range(n):
  li2[i] += int(li[i][1])
li2.sort()

for i in range(n):
  if li2[0] == int(li[i][1]):
    min = i
    break
li = li[min:]+li[:min]

for i in range(n):
  print(li[i][0])
    
  
