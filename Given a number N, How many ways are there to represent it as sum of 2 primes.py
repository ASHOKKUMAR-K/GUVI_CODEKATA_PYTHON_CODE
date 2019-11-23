n = int(input())
def isprime(a):
    flag = True
    for i in range(2, a//2+1):
        if a%i==0:
            flag = False
            break
    return flag
p = []
for i in range(2, n):
    if isprime(i):
        p.append(i)
b = []
count = 0
for i in range(len(p)):
    for j in range(len(p)):
        if p[i] + p[j] == n and (p[i] not in b and p[j] not in b):
            count += 1
            b.append(p[i])
            b.append(p[j])
print(count)
