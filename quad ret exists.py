s = int(input())
n = int(input())
l = [int(x) for x in input().split()]
flag = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for m in range(k+1, n):
                if l[i]+l[j]+l[k]+l[m] == s:
                    flag = True
                    break
if flag:print("YES")
else:print("No")
                    
