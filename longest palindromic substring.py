s = input()
l = []
for i in range(len(s)):
    for j in range(i, len(s)):
        l.append(s[i:j+1])
for i in l:
    if i == i[::-1]:
        ans = i
        break
for i in l:
    if i == i[::-1] and len(i) > len(ans):
        ans = i
print(ans)
