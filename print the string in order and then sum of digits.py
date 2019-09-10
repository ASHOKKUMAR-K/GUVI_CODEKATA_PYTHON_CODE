num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
s = str(input())
sum = 0
for i in s:
  if i not in num:
    print(i, end="")
  else:
    sum += int(i)
print(sum)
