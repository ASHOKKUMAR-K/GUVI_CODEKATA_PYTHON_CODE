(a, b) = map(int, input().split(" "))
ans = int(str(bin(a^b))[2:])
#print(ans, type(ans))
sum = 0
while ans > 0:
    sum += (ans%10)
    ans //= 10
print(sum)
