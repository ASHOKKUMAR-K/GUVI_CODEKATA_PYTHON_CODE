n = int(input())
l = [int(x) for x in input().split()]
min = l[0]
count = l.count(l[0])
for i in range(1, n):
    if count > l.count(l[i]):
        min = l[i]
        count = l.count(l[i])
print(min)
