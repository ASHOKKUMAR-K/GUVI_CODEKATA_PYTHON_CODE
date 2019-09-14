a = input().split("#")
b = input().split("#")
x = int(a[1]) + int(a[2]) + int(a[3])
y = int(b[1]) + int(b[2]) + int(b[3])
if x > y:
    print(a[0])
else:
    print(b[0])
