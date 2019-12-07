def knightPosition(a, b):
    p = []
    if a+1 < 4 and b+2 < 4: p.append((a+1, b+2))
    if a+2 < 4 and b+1 < 4: p.append((a+2, b+1))
    if a+1 < 4 and b-2 >= 0: p.append((a+1, b-2))
    if a+2 < 4 and b-1 >= 0: p.append((a+2, b-1))
    if a-1 >= 0 and b+2 < 4: p.append((a-1, b+2))
    if a-2 >= 0 and b+1 < 4: p.append((a-2, b+1))
    if a-1 >= 0 and b-2 >= 0: p.append((a-1, b-2))
    if a-2 >= 0 and b-1 >= 0: p.append((a-2, b-1))
    return p

ch = [list(input()) for _ in range(4)]
q = int(input())
for _ in range(q):
    (i, j) = map(int, input().split())
    if ch[i][j] == '#':
        print(-1)
        continue
    else:
        count = 0
        l = knightPosition(i, j)
        for k in l:
            if ch[k[0]][k[1]] == '#': continue
            else: count += 1
        print(count)
