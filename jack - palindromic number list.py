n = int(input())
l = input().split()
flag = False
for i in range(n):
    for j in range(i+1, n):
        s = str(l[i]+l[j])
        if s == s[::-1]:
            flag = True
            break
if flag:print("YES")
else:print("NO")
