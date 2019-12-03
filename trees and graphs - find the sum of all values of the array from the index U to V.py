(n, q) = map(int, input().split())
l = [int(x) for x in input().split()]
for _ in range(q):
    (u, v) = map(int, input().split())
    print(sum(l[u-1 : v]))
