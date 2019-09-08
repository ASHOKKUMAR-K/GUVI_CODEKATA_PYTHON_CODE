s1 = str(input())
s2 = str(input())
if (s2 in s1):
    for i in range(len(s1)):
        if s2 == s1[i:(i+3)]:
            ans = i
    print(ans)
else:
    print(-1)
