n = int(input())
l=[]
while n>0:
    l.append(n%10)
    n //= 10
count = 0
flag = False
for i in l:
    count = l.count(i)
    if count > 1:
        flag = True
if flag:
    print("yes")
else:
    print("no")
