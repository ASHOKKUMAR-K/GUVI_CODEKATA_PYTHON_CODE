n = int(input())
l = input().split(" ")
min = int(l[0])
for i in range(n):
    if min > int(l[i]):
        min = int(l[i])
print(min)
