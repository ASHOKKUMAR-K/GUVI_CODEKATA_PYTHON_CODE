l = input().split(" ")
for i in range(len(l)):
    if l[i] == "and":
        (l[i+1], l[i-1]) = (l[i-1], l[i+1])
for i in l:
    print(i, end = " ")
