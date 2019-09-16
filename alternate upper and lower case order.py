l = input().split()
for i in range(len(l)):
    if i % 2 == 0:
        print(l[i].upper(), end = " ")
    else:
        print(l[i], end = " ")
