n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    (op, x, y) = map(int, input().split())
    if op == 1:
        l[x-1] += y
    if op == 2:
        l[x-1] -= y
        if l[x-1] < 0:l[x-1] = 0
    if op == 3:
        if 0 in l[x-1 : y]:print("escape")
        else:print("stay and fight")
