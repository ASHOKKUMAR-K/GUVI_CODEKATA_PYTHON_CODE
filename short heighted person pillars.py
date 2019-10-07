h = int(input())
l = [int(x) for x in input().split()]
count = 0
for i in l:
    if i <= h:
        count+=1
print(count)
