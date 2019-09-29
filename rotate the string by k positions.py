(s,k) = map(str, input().split(" "))
l = []
for i in s:
    l.append(i)
for i in range(int(k)):
    l.insert(0, l.pop(len(l)-1))
for i in l:
    print(i, end = "")
