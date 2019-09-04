k = int(input())
n = 0
while True:
    temp = n
    sm = 0
    while temp > 0:
        sm += (temp%10)
        temp = temp // 10
    if sm == k:
        break
    else:
        n += 1
print(n)
