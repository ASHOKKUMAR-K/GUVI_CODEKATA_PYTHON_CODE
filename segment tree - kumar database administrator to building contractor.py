n = int(input())
l1 = [int(x) for x in input().split()]
l2 = [0 for _ in range(n)]
q = int(input())
for _ in range(q):
    (t, x, y) = map(int, input().split())
    if t == 1:
        l2[x-1] = l2[x-1] + y
        if l2[x-1] > l1[x-1]: l2[x-1] = l1[x-1]
    if t == 2:
        print(max(l2[x-1:y]))
