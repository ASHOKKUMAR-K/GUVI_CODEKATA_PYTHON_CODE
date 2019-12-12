n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(sum(l[:i+1]) + sum(l[i:]))
print(*a)
