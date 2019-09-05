n = int(input())
def isprime(i):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    return flag
a = []
for i in range(2, n):
    if isprime(i) and i%10==3:
        a.append(i)
sum = 0
for i in a:
    sum += i
print(sum)
