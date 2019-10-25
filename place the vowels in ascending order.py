s = str(input())
v = ('a','e','i','o','u')
l = []
for i in s:
    if i in v:
        l.append(i)
l.sort()
j = 0
for i in s:
    if i in v:
        print(l[j], end = "")
        j+=1
    else:
        print(i, end = "")
