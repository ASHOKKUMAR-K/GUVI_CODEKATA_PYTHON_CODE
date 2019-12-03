n = int(input())
l = [[int(x) for x in input().split()] for _ in range(n)]
def neighbourPosition(a, b, n):
    t = []
    for i in range(n):
        for j in range(n):
            if abs(i-a) == 1 or abs(j-b) == 1:
                if abs(i-a) > 1 or abs(j-b) > 1: continue
                else: t.append((i, j))
    return t
count = 0
for p in range(n):
    for q in range(n):
        if l[p][q] == 1:
            flag = True
            z = neighbourPosition(p, q, n)
            for k in z:
                if l[k[0]][k[1]] == 1:
                    flag = False
                    break
            if flag: count += 1
print(count)
        
