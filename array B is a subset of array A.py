n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
flag = True
for i in b:
    if i not in a:
        flag = False
        break
if flag:
    print("yes")
else:
    print("no")
