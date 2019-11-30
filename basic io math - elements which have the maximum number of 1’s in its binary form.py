n = int(input())
l = [int(x) for x in input().split()]
z = int(input())
l.sort(reverse = True)
for i in range(n-1, -1, -1):
    for j in range(i):
        if (str(bin(l[j]))[2:]).count('1') < (str(bin(l[j+1]))[2:]).count('1'):
            (l[j], l[j+1]) = (l[j+1], l[j])
print(*l[:z])
