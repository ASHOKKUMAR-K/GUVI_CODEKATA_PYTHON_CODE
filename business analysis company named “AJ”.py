n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
flag = False
for i in range(n):
    for j in range(n):
        a[i], b[j] = b[j], a[i]
        if sum(a) == sum(b):
            flag = True
            break
if flag:print("Yes")
else:print("No")
