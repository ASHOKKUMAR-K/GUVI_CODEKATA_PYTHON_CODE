(r1, c1) = map(int, input().split())
m1 = [[int(x) for x in input().split()] for _ in range(r1)]
(r2, c2) = map(int, input().split())
m2 = [[int(x) for x in input().split()] for _ in range(r1)]
if r1 == r2 and c1 == c2:
    flag = True
    for i in range(r1):
        for j in range(c1):
            if m1[i][j] != m2[i][j]:
                flag = False
                break
        if not flag:break
    if flag:print("Equal")
    else:print("Not equal")
else:print("Not equal")
