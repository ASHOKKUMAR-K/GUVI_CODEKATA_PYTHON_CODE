n = int(input())
l = [int(x) for x in input().split()]
count = 0
m = 0
for i in range(1, n):
    if l[i] > l[i-1]:
        count += 1
        if m < count:
            m = count
    else:
        count = 0
print(m + 1)
