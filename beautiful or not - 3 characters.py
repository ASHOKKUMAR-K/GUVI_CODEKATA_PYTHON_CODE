a = str(input())
b = []
for i in a:
    if i not in b:
        b.append(i)
if len(b)==3:
    print(1)
else:
    print(0)
