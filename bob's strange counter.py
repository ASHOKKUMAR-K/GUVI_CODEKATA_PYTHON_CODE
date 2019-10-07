n = int(input())
i = 3
temp = i
for j in range(n):
    k = i
    #print(i, end = " -> ")
    if i != 1:
        i-=1
        continue
    else:
        i = temp * 2
        temp = i
        continue
    #print(i)
print(k)
