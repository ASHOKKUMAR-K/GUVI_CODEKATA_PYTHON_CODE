n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = []
for i in range(n):
    c.append(a[i] + b[i])
print(*c)
