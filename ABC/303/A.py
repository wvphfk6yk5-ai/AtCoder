n = int(input())
s = input().strip()
t = input().strip()

for i in range(n):
  if s[i] != t[i]:
    if (s[i] == "1" and t[i] =="l")or(t[i] == "1" and s[i] =="l")or(s[i] == "0" and t[i] =="o") or(s[i] == "o" and t[i] =="0"):
      continue
    else:
      print("No")
      exit()

print("Yes")