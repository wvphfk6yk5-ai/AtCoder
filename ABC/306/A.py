n = int(input())
s = input().strip()
echo = s[0]+s[0]
for i in range(1,n):
  echo+=s[i]+s[i]

print(echo)
  
  