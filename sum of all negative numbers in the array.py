n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
sum = 0
for i in l:
    if i < 0:
        sum += i
print(sum)
