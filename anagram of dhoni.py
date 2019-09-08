l = ['d','h','o','n','i']
s = str(input())
for i in s:
	if i not in l:
		flag = False
		break
	else:
		flag = True
if flag:
	print("yes")
else:
	print("no")
