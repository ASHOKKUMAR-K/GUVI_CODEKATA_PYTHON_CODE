num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
s = input()
flag = True
for i in s:
    if i not in num:
        flag = False
if flag:
    print("yes")
else:
    print("no")
