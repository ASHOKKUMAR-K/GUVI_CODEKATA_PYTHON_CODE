s = str(input())
n = int(input())
for _ in range(n):
    a = str(input())
    st = list(set(sorted(a)))
    cond1 = True
    for i in st:
        if i not in s:
            cond1 = False
            break
    if cond1:
        cond2 = True
        for i in st:
            if a.count(i) > s.count(i):
                cond2 = False
                break
        if cond2: print("YES")
        else:print("NO")
    else:print("NO")
