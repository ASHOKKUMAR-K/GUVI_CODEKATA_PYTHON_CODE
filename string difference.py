(a, b, c) = map(str, input().split(" "))
ln = len(a)
count = 0
for i in range(ln):
    if a[i] != b[i]:
        count += 1
#print(count)
if count == int(c):
    print("yes")
else:
    print("no")
