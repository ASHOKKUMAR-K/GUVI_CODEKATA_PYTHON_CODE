n = int(input())
a = bin(n)[2:]
count = 0
for i in a[::-1]:
    count += 1
    if i == '1':
        break
print(count)
