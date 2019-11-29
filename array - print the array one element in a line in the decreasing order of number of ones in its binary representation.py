n = int(input())
l = [int(x) for x in input().split()]
for i in range(n-1, -1, -1):
    for j in range(i):
        a = (str(bin(l[j]))[2:]).count('1')
        b = (str(bin(l[j+1]))[2:]).count('1')
        if a > b: continue
        elif b > a: (l[j], l[j+1]) = (l[j+1], l[j])
        else:
            if l[j] >= l[j+1]: continue
            else: (l[j], l[j+1]) = (l[j+1], l[j])
for i in l:
    print(i)
