n = int(input())
l = [int(x) for x in input().split()]
f = l[0] + l[1] + l[2]
la = l[-1] + l[-2] + l[-3]
if f == la:
  print(1)
else:
  print(0)
