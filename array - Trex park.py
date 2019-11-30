(r, c) = map(int, input().split())
l = [int(x) for x in input().split()]
p = [[str(x) for x in input().split()] for _ in range(r)]
tot_G = 0
for i in range(r):
    for j in range(c):
        if p[i][j] == 'G': tot_G += 1
gate = []
for i in range(0, 8, 2):
    gate.append((l[i]-1, l[i+1]-1))
import random
for i in range(r):
    for j in range(c):
        if (i, j)==gate[0] or (i, j)== gate[1] or (i, j)== gate[2]:
            p[i][j] = 'E'
        elif (i, j) == gate[3]: p[i][j] = 'T'
        else: continue
#[print(*i) for i in p]
safe_idx = 0
for i in p: safe_idx += (i.count('E'))
r = random.choice([2,4])
ans = ((tot_G - r) / tot_G) * 100
print("{:0.2f}".format(ans))
