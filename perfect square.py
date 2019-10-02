l = [x**2 for x in range(50)]
(a,b) = map(int, input().split())
if (a*b) in l:
    print("yes")
else:
    print("no")
