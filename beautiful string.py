s = str(input())
l = len(s)
if (s[0] == 'a' or s[0] == 'A') and (s[l//2] == 'm' or s[l//2] == 'M') and (s[l-1] == 'z' or s[l-1] == 'Z'):
	print("1")
else:
	print("0")
