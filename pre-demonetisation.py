n = int(input())
count = 0
while n >= 1000:
    count += 1
    n -= 1000
while n >= 500:
    count += 1
    n -= 500
while n >= 100:
    count += 1
    n -= 100
while n >= 50:
    count += 1
    n -= 50
while n >= 10:
    count += 1
    n -= 10
while n >= 1:
    count += 1
    n -= 1
print(count)