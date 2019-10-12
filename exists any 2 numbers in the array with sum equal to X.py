(n, x) = map(int, input().split())
l = [int(x) for x in input().split()]
flag = False
for i in range(n):
    for j in range(i+1, n):
        if l[i]+l[j] == x:
            flag = True
if flag:
    print("yes")
else:
    print("no")
