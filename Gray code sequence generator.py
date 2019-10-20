n = int(input())
def generateGrayCode(n):
    l = ['0', '1']
    if n==1:
        ans = l
    else:
        for k in range(1, n):
            a = []
            a.extend(l)
            l.reverse()
            a.extend(l)
            b = []
            for i in range(len(a)//2):
                b.append('0' + a[i])
            for i in range(len(a)//2, len(a)):
                b.append('1' + a[i])
            l = b
            ans = b
    return ans
lst = generateGrayCode(n)
print(*lst)
