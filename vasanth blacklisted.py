n = int(input())
l = [str(x) for x in input().split()]
p = l.count('P')
a = l.count('a')
at = (p/n)*100
if at <= 25:
	print("Blacklisted")
else:
	print("Not Blacklisted")
