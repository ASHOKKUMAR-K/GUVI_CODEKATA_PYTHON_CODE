a = input().split(" ")
N = int(a[0])
K = int(a[1])
b = input().split(" ")
count = 0
for i in range(N):
    if K == int(b[i]):
        count += 1
print(count)
