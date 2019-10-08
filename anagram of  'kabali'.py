n = int(input())
l = []
for i in range(n):
    l.append(str(input()))
ref = 'kabali'
count = 0
for i in l:
    flag = True
    for j in i:
        if i.count(j) != ref.count(j):
            flag = False
            break
    if flag:
        count+=1
print(count)
