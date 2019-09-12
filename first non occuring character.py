s = str(input())
count = 0
for i in range(len(s)):
    count = s.count(s[i])
    if count == 1:
        ans = s[i]
        break
print(ans)
