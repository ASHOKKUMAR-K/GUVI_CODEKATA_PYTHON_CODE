n = int(input())
l = [int(x) for x in input().split()]
max = l[0]+l[1]
for i in range(n-1):
    sum = l[i]+l[i+1]
    if sum > max:
        max = sum
print(max)
