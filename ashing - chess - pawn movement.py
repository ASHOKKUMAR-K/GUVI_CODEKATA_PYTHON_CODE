ch = [list(input()) for _ in range(4)]
q = int(input())
for _ in range(q):
    (i, j) = map(int, input().split())
    if ch[i][j] == '#':
        print(-1)
        continue
    else:
        count = 0
        while True:
            if i-1 >= 0:i -= 1
            else: break
            if ch[i][j] == '#': break
            else: count += 1
        print(count)
