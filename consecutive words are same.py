n = int(input())
a = []
for i in range(n):
    a.append(str(input()))
print(a)
flag = False
for i in range(n-1):
        if a[i] == a[i+1]:
            flag = True
if flag:
    print("yes")
else:
    print("no")
