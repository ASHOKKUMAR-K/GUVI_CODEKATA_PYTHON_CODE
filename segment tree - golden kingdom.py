n = int(input())
l = [int(x) for x in input().split()]
q = int(input())
for _ in range(q):
    a = [int(x) for x in input().split()]
    if a[0] == 1:
        if l[a[1]-1] == 0: l[a[1]-1] = 1
        else:l[a[1]-1] = 0
    if a[0] == 2:
        x = l[a[1]-1 : a[2]].count(1)
        y = l[a[1]-1 : a[2]].count(0)
        if x == y:print("Neutral")
        elif x > y:print("Satisfied")
        else:print("Dissatisfied")
