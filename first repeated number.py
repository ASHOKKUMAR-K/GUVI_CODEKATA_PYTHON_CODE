n = int(input())
l = input().split(" ")
flag = False
for i in range(n):
    count = l.count(l[i])
    if count > 1:
        flag = True
        ans = l[i]
        break
if flag:
    print(ans)
else:
    print("unique")
