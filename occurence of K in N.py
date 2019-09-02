(n, k) = map(str, input().split(" "))
count = 0
for i in n:
    if i == k:
    	count += 1
print(count)
