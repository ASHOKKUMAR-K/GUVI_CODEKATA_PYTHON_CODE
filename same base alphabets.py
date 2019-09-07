(s1, s2) = map(str, input().split(" "))
a = []
for i in range(len(s1)):
    a.append(s1[i])
for i in range(len(s2)):
    if s2[i] not in a:
        flag = False
        break
    else:
        flag = True
if flag:
    print("true")
else:
    print("false")
