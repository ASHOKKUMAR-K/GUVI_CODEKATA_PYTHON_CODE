n = int(input())
l = [int(x) for x in input().split()]
l.sort()
m = count = 0
for i in range(n-1):
    if l[i+1] == l[i]+1:
        count += 1
        if m < count:
            m = count
    else:
        count = 0
print(m+1)
