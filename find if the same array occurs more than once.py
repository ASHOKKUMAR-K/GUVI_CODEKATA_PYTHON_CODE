n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append([int(x) for x in input().split()])
flag = False
for i in l:
    if l.count(i) > 1:
        flag = True
        break
if flag:print("YES")
else:print("NO")
