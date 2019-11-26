(n, q, m) = map(int, input().split())
l = [int(x) for x in input().split()]
for _ in range(q):
    (op, x, y) = map(int, input().split())
    if op == 1:
        l.insert(x-1, l.pop(y-1))
    if op == 2:
        c = []
        for i in range(y-x+1):
            c.append(l.pop(x-1))
        for i in c:
            l.insert(x-1, i)
ans = []
b = [int(x) for x in input().split()]
for i in b:
    ans.append(l[i-1])
print(*ans, end = " ")
