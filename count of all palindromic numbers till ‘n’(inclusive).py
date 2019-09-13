n = int(input())
count = 0
for i in range(1, n+1):
    i = str(i)
    if i == i[::-1]:
        count += 1
print(count)
