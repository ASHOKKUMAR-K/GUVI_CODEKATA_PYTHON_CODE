(s, k) = map(str, input().split(" "))
for i in range(len(s)):
    if s[i] == k:
        ans = i+1
        break
print(ans)
