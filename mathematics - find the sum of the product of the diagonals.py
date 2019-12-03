n = int(input())
l = [[int(x) for x in input().split()] for _ in range(n)]
prod1 = 1
for i in range(n):
    prod1 *= l[i][i]
i = 0
j = n-1
prod2 = 1
while True:
    prod2 *= l[i][j]
    if i == n-1: break
    i += 1
    j -= 1
print(prod1 + prod2)
