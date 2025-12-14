n = int(input())
s = input().strip()
cnt_T=0
cnt_A=0

for x in s:
  if cnt_A == n//2+n%2 or cnt_T ==n//2+n%2:
    break
  if x == "A":
    cnt_A += 1
  else:
    cnt_T += 1

win=max(cnt_A,cnt_T)
if win ==cnt_A:
  print("A")
else:
  print("T")