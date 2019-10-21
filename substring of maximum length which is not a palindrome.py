s = str(input())
n = len(s)
l = []
for i in range(n):
    for j in range(i, n):
        l.append(s[i:j+1])
ans = l[0]
for i in range(1, len(l)):
    if l[i] != l[i][::-1] and len(ans) < len(l[i]):
        ans = l[i]
print(ans)
