n = int(input())
a = []
while n>0:
    digit = n % 10
    if digit % 2 != 0:
        a.append(digit)
    n //= 10
#print(a)
sum = 0
for i in a:
    sum += i
#print(sum)
if sum % 2 == 0:
    print("E")
else:
    print("O")
