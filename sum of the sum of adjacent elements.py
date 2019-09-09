n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
sum = 0
for i in range(len(l)-1):
    sum += (l[i] + l[i+1])
print(sum)
