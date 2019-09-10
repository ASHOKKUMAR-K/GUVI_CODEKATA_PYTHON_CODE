s = str(input())
l = []
for i in s:
    count = s.count(i)
    if count == 1:
        l.append(i)
for i in l:
    print(i, end = "")
