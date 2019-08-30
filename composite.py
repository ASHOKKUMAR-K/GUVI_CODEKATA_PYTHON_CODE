a = int(input())
flag = False
for i in range(2, int(a/2)):
    if a % i == 0:
        flag = True
if flag:
    print("yes")
else:
    print("no")
