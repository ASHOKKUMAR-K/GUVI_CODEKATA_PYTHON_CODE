n = int(input()) 
l = [int(x) for x in input().split()] 
q = int(input()) 
for _ in range(q):
    a = [int(x) for x in input().split()] 
    if a[0] == 1:
        l[a[1]-1] = l[a[1]-1] - a[2]
        if l[a[1]-1] < 0:l[a[1]-1]=0 
    if(a[0]==2):
        print(max(l[a[1]-1:a[2]]))
