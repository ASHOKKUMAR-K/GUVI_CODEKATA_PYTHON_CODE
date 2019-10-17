n = int(input())
def prime(n):
    i = 2
    l = []
    while n>0:
        if i == 2 or i == 3:
            l.append(i)
            n -= 1
        else:
            flag = True
            for j in range(2, i//2+1):
                if i%j==0:
                    flag = False
                    break
            if flag:
                l.append(i)
                n-=1
        i+=1
    return l
lst = prime(n)
a = []
sum = 0
for i in lst:
    sum += i
    a.append(sum)
print(*a)
