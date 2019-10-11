n = int(input())
l = [int(x) for x in input().split()]
sum = 0
for i in range(n-1):
    sum += max(l[i], l[i+1])
print(sum)
