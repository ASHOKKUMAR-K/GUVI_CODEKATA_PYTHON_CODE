s = input().split()
ans = s[0]
for i in range(len(s)):
    if len(s[i]) > len(ans):
        ans = s[i]
print(ans)
