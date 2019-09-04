n = int(input())
count = 0
temp = n
while temp > 0:
    count += 1
    temp //= 10
sum = 0
while n > 0:
    digit = n%10
    sum += (digit ** count)
    n //= 10
print(sum)
