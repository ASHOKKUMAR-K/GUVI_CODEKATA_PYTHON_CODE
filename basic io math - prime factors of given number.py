n = int(input())
def isprime(a):
    flag = True
    for i in range(2,(a//2)+1):
        if a % i == 0:
            flag = False
    return flag
factor = []
for i in range(2,n+1):
    if n % i == 0:
        factor.append(i)
#print(*factor)
prime_factor = []
for i in factor:
    if isprime(i):
        prime_factor.append(i)
prime_factor.sort()
print(*prime_factor)
