n = int(input())
l = [int(x) for x in input().split()]
m = int(input())
a = [int(x) for x in input().split()]
for i in a:
     if i in l:
          print(l.count(i), end = " ")
     else:
          print("Not Present", end = " ")
