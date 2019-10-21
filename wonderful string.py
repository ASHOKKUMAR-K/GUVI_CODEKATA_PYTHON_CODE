s = str(input())
l = []
for i in s:
    if i not in l:
        l.append(i)
if len(l)==3:print("Wonder")
else:print(-1)
