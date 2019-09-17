(s, a) = map(str, input().split())
if len(s) < len(a):
    ln = len(s)
else:
    ln = len(a)
l = []
for i in range(ln):
    if s[i] == a[i]:
        l.append(s[i])
for i in l:
    print(i, end = "")
