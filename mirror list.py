n = int(input())
f = input().split(" ")
s = input().split(" ")
a = [int(x) for x in f]
b = [int(y) for y in s]
#print(a[1])
b.sort()
#print(b[1])
flag = True
for i in range(n):
    if a[i] != b[i]:
        flag = False
if flag:
    print("yes")
else:
    print("no")
