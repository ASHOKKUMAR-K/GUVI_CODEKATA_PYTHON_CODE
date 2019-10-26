(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
i = 1
count = 0
a = []
while count < 3:
    if k-i in l:
        a.append(k-i)
        count += 1
    if k+i in l and count < 3:
        a.append(k+i)
        count += 1
    i += 1
print(*a)    
