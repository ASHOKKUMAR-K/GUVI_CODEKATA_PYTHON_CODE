n = int(input()) 
l = []
for _ in range(n):
    l.append(str(input())) 
q = int(input()) 
r = []
for i in range(q):
    r.append(str(input())) 
for i in range(q):
    t = r[i]
    c = 0 
    ans = "" 
    first = 0
    for j in range(len(l)):
        f = 1
        for k in range(len(t)):
            if t[k] != l[j][k]:
                f = 0 
                break 
        if f == 1:
            c = c + 1 
            if first == 0:
                ans = l[j] 
                first = 1 
    if c == 0:
        print(t)
    if c == 1:
        print(ans) 
    if c > 1:
        print(ans, end="")
        print("+")
