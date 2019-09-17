(n, k) = map(str, input().split())
flag = True
for i in range(int(k)+1):
    if str(i) not in n:
        flag = False
        break
if flag:
    print("yes")
else:
    print("no")
