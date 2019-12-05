n = int(input())
l = [int(x) for x in input().split()]
max = l[0]
m = 0
for i in range(n):
    if max <= l[i]:
        max = l[i]
        m = i
print(m)
