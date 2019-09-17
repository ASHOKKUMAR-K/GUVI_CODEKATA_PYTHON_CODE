s = str(input())
max = s.count(s[0])
ans = s[0]
for i in s:
    ct = s.count(i)
    if ct > max:
    	max = ct
    	ans = i
print(ans)
