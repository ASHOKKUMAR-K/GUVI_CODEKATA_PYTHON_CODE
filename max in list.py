n = int(input())
l = input().split(" ")
max = int(l[0])
for i in range(n):
    if max < int(l[i]):
        max = int(l[i])
print(max)
