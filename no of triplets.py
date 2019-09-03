n = int(input())
l = input().split(" ")
a = []
for i in range(n):
    if int(l[i]) not in a:
        a.append(int(l[i]))
#a.sort()
#print(a)
count = 0
ln = len(a)
for i in range(ln):
    for j in range(i+1, ln):
        for k in range(j+1, ln):
            if (a[i] < a[j]) and (a[j] < a[k]):
                #print(a[i], a[j], a[k])
                count += 1
print(count)
