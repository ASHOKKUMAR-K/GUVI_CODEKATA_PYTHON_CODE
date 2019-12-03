s = list(str(input()))
z = 1
while z == 1:
    z = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            z = 1
            idx = i
    if z == 1:
        s.pop(idx)
        s.pop(idx)
    if len(s) < 2: break
if len(s) != 0:
    ans = ""
    for i in s: ans += i
    print(ans)
else: print("-1")
