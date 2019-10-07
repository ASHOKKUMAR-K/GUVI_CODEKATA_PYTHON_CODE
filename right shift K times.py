(n, k) = map(int, input().split())
l = input().split()
for i in range(k):
    l.insert(0, l.pop())
print(*l)
