n = int(input())
l1 = input().split()
m = int(input())
l2 = input().split()
flag = True
for i in l2:
    if i not in l1:
        flag = False
        break
if flag:print("Yes")
else:print("No")
