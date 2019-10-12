n = int(input())
l = [int(x) for x in input().split()]
b = []
flag = False
for i in l:
    if l.count(i)>1 and i not in b:
        flag = True
        b.append(i)
if flag:
    b.sort()
    print(*b)
else:
    print("unique")
