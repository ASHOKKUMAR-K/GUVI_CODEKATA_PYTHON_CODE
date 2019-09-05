n = int(input())
sum = 0
while n > 0:
    sum += (n%10)
    n //= 10
print(sum)
if (sum>=1) and (sum <= 9):
    print("YES")
else:
    sum = str(sum)
    rev = sum[::-1]
    if sum == rev:
        print("YES")
    else:
        print("NO")
