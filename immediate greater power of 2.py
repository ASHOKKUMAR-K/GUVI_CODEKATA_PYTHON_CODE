n = int(input())
lst =[(2**x) for x in range(10)]
#print(*lst)
for i in lst:
    if i > n:
        print(i)
        break
