n = int(input())
l = [int(x) for x in input().split()]
a = [x for x in range(1, n+1)]
flag = True
for i in a:
    if i not in l:
        flag = False
        break
if flag:print("yes")
else:print("no")
