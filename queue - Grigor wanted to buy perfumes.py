(n, q) = map(int, input().split())
l = [int(x) for x in input().split()]
count = 0
price = 0
for _ in range(q):
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        mn = 0
        for i in range(len(l)):
            if l[mn] > l[i]:
                mn = i
        l[mn] += a[1]
    if a[0] == 2:
        count += 1
        mn = 0
        for i in range(len(l)):
            if l[mn] > l[i]:
                mn = i
        price += l[mn]
print(count, price)
