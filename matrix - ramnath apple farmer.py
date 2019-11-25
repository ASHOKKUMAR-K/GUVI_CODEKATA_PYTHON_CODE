(r, c) = map(int, input().split())
l = [[str(x) for x in input().split()] for _ in range(c)]
for i in range(c):
    if "x" in l[i]:
        l[i][0] = "X"
        for j in range(1, r):
            l[i][j] = "x"
    else:l[i][0] = "A"
for i in l:
    print(*i)
