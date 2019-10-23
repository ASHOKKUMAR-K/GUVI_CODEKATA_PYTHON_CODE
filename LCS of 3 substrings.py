(s1, s2, s3) = map(str, input().split())
l = []
for i in range(len(s1)):
    for j in range(i, len(s1)):
        l.append(s1[i:j+1])
flag = True
for i in l:
    if i in s2 and i in s3:
        ans = i
        flag = False
        break
if flag:print(-1)
else:
    for i in l:
        if i in s2 and i in s3 and len(ans) < len(i):
            ans = i
    print(ans)
