n = int(input())
l = []
for i in range(n):
    l.append(str(input()))
k = [] 
q = int(input())
for i in range(q):
    k.append(str(input())) 
for i in range(len(k)): 
    r=[]
    for j in range(len(l)):
        f=1 
        for z in range(len(k[i])):
            if l[j][z] != k[i][z]:
                f=0 
                break 
        if f == 1:
            r.append(l[j])
    if len(r) > 0:
        r.sort() 
        print(r[0])
    else:
        print(k[i])
