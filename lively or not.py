n = int(input())
temp = n
l = []
while temp > 0:
    l.append(temp%10)
    temp //= 10
l.reverse()
#print(*l)
a = []
for i in l:
    if i not in a:
        a.append(i)
#print(*a)
flag = True
for i in a:
    if l.count(a[0])!=l.count(i):
        flag = False
        break
if flag:print(1)
else:print(0)
