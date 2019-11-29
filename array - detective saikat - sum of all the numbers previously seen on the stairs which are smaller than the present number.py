n = int(input())
l = [int(x) for x in input().split()]
sum = 0
for i in range(n):
    for j in range(i):
        if l[j] < l[i]:
            sum += l[j]
print(sum)
