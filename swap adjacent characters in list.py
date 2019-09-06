n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
if n % 2 != 0:
    for i in range(0, n-1, 2):
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp
else:
    for i in range(0, n, 2):
        temp = l[i]
        l[i] = l[i+1]
        l[i+1] = temp
for i in l:
    print(i, end = " ")
