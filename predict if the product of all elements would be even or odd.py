n = int(input())
l = [int(x) for x in input().split()]
flag = False
for i in range(n):
    if l[i]%2==0:
        flag = True
        break
if flag:
    print("even")
else:
    print("odd")
