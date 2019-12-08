(n, q) = map(int, input().split())
l = [int(x) for x in input().split()]
for _ in range(q):
    x = int(input())
    a = []
    for i in l:
        a.append(x^i)
    print(max(a))
