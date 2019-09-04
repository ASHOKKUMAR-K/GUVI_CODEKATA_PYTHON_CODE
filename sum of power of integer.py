n = str(input())
sum = 0
for i in range(len(n)):
    sum += (int(n[i]) ** i)
print(sum)
