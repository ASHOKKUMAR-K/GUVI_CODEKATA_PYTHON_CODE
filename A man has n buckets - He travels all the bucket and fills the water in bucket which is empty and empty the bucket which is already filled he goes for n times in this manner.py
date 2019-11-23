n = int(input())
l = [0 for i in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if j % i == 0:
            if l[j-1] == 0:
                l[j-1] = 1
            else:
                l[j-1] = 0
print(l.count(1))
