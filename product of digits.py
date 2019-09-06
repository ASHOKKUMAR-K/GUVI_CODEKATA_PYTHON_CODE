n = int(input())
pro = 1
while n>0:
	pro *= (n%10)
	n //= 10
print(pro)
