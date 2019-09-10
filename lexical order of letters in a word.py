n = int(input())
s = str(input())
l = []
for i in s:
    l.append(i)
l.sort()
for i in l:
    print(i, end="")
