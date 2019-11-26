n = int(input())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    (op, x, y) = map(int, input().split())
    if op == 1:
        l2[x-1] += y
        
    if op == 2:
        l2[x-1] -= y
        if l2[x-1] < 0:l2[x-1] = 0
    if op == 3:
        flag = True
        for i in range(x-1, y):
            if l2[i] < l1[i]:
                flag = False
                break
        if flag:print("All offices at full efficiency")
        else:print("Understaffed offices present")
