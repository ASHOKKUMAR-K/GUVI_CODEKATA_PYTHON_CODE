s = str(input())
e = []
o = []
for i in range(len(s)):
    if i % 2 == 0:
        e.append(s[i])
    else:
        o.append(s[i])
for i in e:
    print(i, end = "")
print(" ", end = "")
for i in o:
    print(i, end = "")
