(n, k)= map(int, input().split())
l = [int(x) for x in input().split()]
a = []
for i in range(k):
    a.append(l.pop(0))
a.sort()
l.sort(reverse=True)
print(*a,*l)
