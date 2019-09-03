(n, la, r) = map(int, input().split(" "))
l = input().split()
min = int(l[la])
for i in range(la, r):
    if min > int(l[i-1]):
        min = int(l[i-1])
print(min)
