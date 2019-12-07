n = int(input())
r = [int(x) for x in input().split()]
s = [str(x) for x in input().split()]
d = {}
for i in range(n):
    d[r[i]] = s[i]
na = int(input())
f = {}
for _ in range(na):
    (a, b) = map(str, input().split())
    f[a] = int(b)
r.sort()
for i in r:
    if d[i] in f: ans = f[d[i]]
    else: ans = -1
    print(i, ans)
