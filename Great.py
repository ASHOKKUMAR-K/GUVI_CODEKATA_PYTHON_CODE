n = int(input())
a = n
sum = 0
pro = 1
while n > 0:
    digit = n % 10
    sum += digit
    pro *= digit
    n //= 10
if (sum+pro) == a:
    print("Great")
else:
    print("Not")
