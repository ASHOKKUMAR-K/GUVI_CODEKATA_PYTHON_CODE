(l, r) = map(int, input().split())
arm = []
flag = False
for i in range(l, r+1):
    num = i
    sm = 0
    p = len(str(num))
    while num > 0:
        sm += (num % 10) ** p
        num //= 10
    if sm == i:
        flag = True
        arm.append(i)
if flag:print(*arm)
else: print("No elements")
