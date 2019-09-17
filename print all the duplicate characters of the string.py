s = str(input())
l = []
for i in s:
    c = s.count(i)
    if c > 1 and i not in l:
    	l.append(i)
flag = False
for i in s:
    c = s.count(i)
    if c > 1:
    	flag = True
if flag:
    print(*l)
else:
    print("-1")
