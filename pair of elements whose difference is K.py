(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
count = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if abs(l[i]-l[j])==k:
            count += 1
print(count)
