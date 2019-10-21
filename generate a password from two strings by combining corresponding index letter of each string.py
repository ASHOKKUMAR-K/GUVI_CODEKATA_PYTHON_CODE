s1, s2 = map(str, input().split())
if len(s1) != len(s2):
    m = abs(len(s1) - len(s2))
    if len(s1) < len(s2):
        for i in range(m):
            s1 += str(i+1)
    else:
        for i in range(m):
            s2 += str(i+1)
for i in range(len(s1)):
    print(s1[i], end = "")
    print(s2[i], end = "")
