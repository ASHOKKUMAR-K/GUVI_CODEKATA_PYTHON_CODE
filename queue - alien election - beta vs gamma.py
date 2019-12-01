n = int(input())
c = [int(x) for x in input().split()]
beta = 0
gamma = 0
def maxIndex(c):
    idx = 0
    for k in range(len(c)):
        if c[idx] < c[k]:
            idx = k
    return idx
flag = False
while True:
    beta += c[maxIndex(c)]
    c[maxIndex(c)] //= 3
    if beta >= 1000:
        flag = True
        print("Beta")
        break
    gamma += c[maxIndex(c)]
    c[maxIndex(c)] //= 3
    gamma += c[maxIndex(c)]
    c[maxIndex(c)] //= 3
    if gamma >= 1000:
        flag = True
        print("Gamma")
        break
    if max(c) == 0: break
if not flag: print("-1")
