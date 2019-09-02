#Given a number N and an array of N numbers, find the number of pairs such ai + aj = ak for all i < j < k.

n = int(input())
l = input().split(" ")
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (int(l[i]) + int(l[j])) == int(l[k]):
                count += 1
print(count)
