n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
sum1 = 0
for i in range(n):
    sum1 += l[i][i]
j = n-1
sum2 = 0
for i in range(n):
    sum2 += l[i][j]
    j -= 1
print(sum1 * sum2)
