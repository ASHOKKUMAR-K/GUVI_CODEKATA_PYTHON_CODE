n = int(input())
l = [int(x) for x in input().split()]
a,b=l[0],l[1]
minsum = abs(l[0] + l[1])
for i in range(n):
    for j in range(i+1, n):
        if minsum > abs(l[i] + l[j]):
            minsum = abs(l[i] + l[j])
            a, b = l[i], l[j]
print(a,b)
