n = int(input())
a=[]
for i in range(n):
    s = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    a.extend(l)
print(*a)
