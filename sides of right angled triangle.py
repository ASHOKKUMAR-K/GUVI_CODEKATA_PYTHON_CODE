l = [int(x) for x in input().split()]
l.sort()
if (l[0]**2 + l[1]**2) == l[2]**2:
	print("yes")
else:
	print("no")
