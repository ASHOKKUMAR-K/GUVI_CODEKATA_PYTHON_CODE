n = int(input())
l = input().split(" ")
count = l.count(l[0])
a=[]
for i in l:
    ct = l.count(i)
    if ct <= count:
        count = ct
        a.append(i)
a.sort(reverse = True)
print(*a)
