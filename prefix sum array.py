n = int(input())
l = [int(x) for x in input().split()]
sum = 0
for i in range(n):
	sum += l[i]
	print(sum, end = " ")
