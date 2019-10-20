n = int(input())
l = input().split()
count = 0
for i in range(n):
    for j in range(i, n):
        count+=1
print(count)
