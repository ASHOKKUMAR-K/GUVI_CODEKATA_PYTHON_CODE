l = input().split(" ")
ct = l.count(l[0])
ans = l[0]
for i in l:
    count = l.count(i)
    if ct < count:
        ans = i
        ct = count
print(ans, ct)
