n = int(input())
l = input().split(" ")
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (int(l[i]) + int(l[j])) == int(l[k]):
                print(l[i], l[j], l[k])
