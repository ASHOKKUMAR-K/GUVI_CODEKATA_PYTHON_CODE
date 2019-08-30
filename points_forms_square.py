(x1, y1) = map(int, input().split(" "))
(x2, y2) = map(int, input().split(" "))
(x3, y3) = map(int, input().split(" "))
(x4, y4) = map(int, input().split(" "))
#print(y1, y2, y3, y4, x1, x4, x2, x3)
if (y1 == y4 and y2 == y3 and x1 == x2 and x3 == x4):
    print("yes")
else:
    print("no")
