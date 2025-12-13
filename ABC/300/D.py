import bisect

def eratosthenes(n):
    is_prime =[False,False]+[True] * (n-1)
    
    for i in range(2,int(n**0.5)+1):
      if is_prime[i]:
        for j in range(i*i,n+1,i):
          is_prime[j]=False
    
    return [i for i in range(n+1) if is_prime[i]]

N=int(input())
m=int(N**0.5)+1
primes=eratosthenes(m)
M=len(primes)

ans=0

for i in range(M-2):
  a=primes[i]
  if a**5>N:
    break
  for j in range(i+1,M-1):
    b=primes[j]
    denom=a**2*b
    if denom*b**2 > N:
      break
    
    limit=N//denom
    c_max=int(limit**0.5)
    k=bisect.bisect_right(primes,c_max)-1
    if k > j:
      ans += k-j

print(ans)

    
    
    
