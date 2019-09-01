(l,r) = map(int, input().split(" "))
sum = 0
for i in range(l, r+1):
    if i % 2 == 1:
    	sum = sum + i
print(sum)
