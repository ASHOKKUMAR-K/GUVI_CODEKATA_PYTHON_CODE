n = int(input())
reg = [int(x) for x in input().split()]
mark = [int(x) for x in input().split()]
d = {}
for i in range(n):
    d[reg[i]] = 0
for i in range(n-1, -1, -1):
    for j in range(i):
        if reg[j] > reg[j+1]:
            reg[j], reg[j+1] = reg[j+1], reg[j]
            d[reg[j]] += 1
            d[reg[j+1]] += 1
for i in range(n):
    mark[i] -= d[reg[i]]
print(*mark)
