a = str(input())
for i in range(len(a)):
  if a[i] == 'a' or a[i] == 'b':
    flag = True
    pass
  else:
    flag = False
    break
if flag:
  print("yes")
else:
  print("no")
