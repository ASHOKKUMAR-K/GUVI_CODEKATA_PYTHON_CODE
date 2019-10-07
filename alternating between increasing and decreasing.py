n = int(input())
l = [int(x) for x in input().split()]
flag = True
for i in range(len(l)-1):
    if i % 2 == 0:
        if l[i] > l[i+1]:
            flag = False
            break
    if i % 2 != 0:
        if l[i] < l[i+1]:
            flag = False
            break
if flag:print("yes")
else:print("no")
