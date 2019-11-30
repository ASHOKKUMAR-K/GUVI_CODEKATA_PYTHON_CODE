n = input()
l = len(n)
n = int(n)
s = 0
while n > 0:
    s += ((n%10)**l)
    n //= 10
print(s)
