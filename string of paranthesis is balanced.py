s = str(input())
if (s.count('(') == s.count(')') and s.count('{') == s.count('}')) and s.count('[') == s.count(']'):
	print("yes")
else:
	print("no")
