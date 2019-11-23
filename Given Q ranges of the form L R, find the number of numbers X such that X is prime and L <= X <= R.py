n = int(input())
def isprime(a):
    flag = True
    for i in range(2, a):
        if a % i == 0:
            flag = False
            break
    return flag
for i in range(n):
    count = 0
    (l, r) = map(int, input().split())
    for i in range(l, r+1):
        if isprime(i) and i != 0 and i != 1:
            count+=1
    print(count)
