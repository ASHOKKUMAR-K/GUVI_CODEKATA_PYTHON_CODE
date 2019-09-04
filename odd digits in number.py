#odd digits in number
n = int(input())
a=[]
l = []
while n>0:
    d = n%10
    l.insert(0, d)
    n = n // 10
for i in l:
    if i % 2 != 0:
        a.append(i)
for i in a:
    print(i, end=" ")
