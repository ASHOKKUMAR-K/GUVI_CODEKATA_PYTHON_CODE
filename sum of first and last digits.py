n = int(input())
l = []
while n > 0:
    digit = n % 10
    l.append(digit)
    n //= 10
print(l[0] + l[len(l)-1])
