(r, c) = map(int, input().split())
l = []
for i in range(r):
    l.append([int(x) for x in input().split()])
a = []
for i in range(r):
    for j in range(c):
        if i == j:
            a.append(l[i][j])
for i in range(r):
    for j in range(c):
        if i+j == r-1 and i!=j:
            a.append(l[i][j])
print(*a)
