n, x = map(int, input().split())
e = int(input())
l = [x for _ in range(n)]
for _ in range(e):
    (op, x, y) = map(int, input().split())
    if op == 1:
        for i in range(x, y+1):
            l[i-1] = l[i-1] - 1
    if op == 2:
        print(sum(l[x-1:y]))
