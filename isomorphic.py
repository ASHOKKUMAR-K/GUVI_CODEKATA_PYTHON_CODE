(s2, s1) = map(str, input().split())
if len(s1) != len(s2):
    print("no")
else:
    l = []
    d = {}
    flag = True
    for i in range(len(s1)):
        if s1[i] not in l:
            l.append(s1[i])
            d[s1[i]] = s2[i]
        else:
            if d[s1[i]] != s2[i]:
                flag = False
                break
    if flag:print("yes")
    else:print("no")
