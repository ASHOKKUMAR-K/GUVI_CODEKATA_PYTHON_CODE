n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    (a, b) = map(int, input().split())
    flag = True
    for i in range(a, b):
        if l[a-1] <l[i]:
            flag = False
            break
    if flag:print("YES")
    else:print("NO")
