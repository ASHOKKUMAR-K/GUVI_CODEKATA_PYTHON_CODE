(r, c) = map(int, input().split())
m = [[int(x) for x in input().split()] for _ in range(r)]
for i in range(c):
    a = []
    for j in range(r):
        a.append(m[j][i])
    print(*a)
