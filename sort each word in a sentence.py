l = input().split(" ")
for i in l:
    a = []
    for j in i:
        a.append(j)
    a.sort()
    for k in a:
        print(k, end= "")
    print(end = " ")
