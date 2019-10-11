n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n//2):
    a.append(l.pop(0))
a.sort()
l.sort(reverse = True)
print(*a, *l)
