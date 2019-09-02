n = int(input())
l = input().split(" ")
b=[]
for i in l:
    if int(i) not in b:
        b.append(int(i))
for i in b:
    print(i, end=" ")
