I = input().split(" ")
A = int(I[0])
B = int(I[1])
C = int(I[2])
l = []
l.append(A)
l.append(B)
l.append(C)
l.sort()
lhs = (l[0] ** 2) + (l[1] ** 2)
rhs = (l[2] ** 2)
if lhs == rhs:
	print("yes")
else:
	print("no")
