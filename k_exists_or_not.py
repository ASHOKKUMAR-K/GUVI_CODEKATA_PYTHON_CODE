#program to check if k exists or not
a = input().split(" ")
N = int(a[0])
K = int(a[1])
b = input().split(" ")
flag = 0
for i in range(N):
    if K == int(b[i]):
        flag = 1
if flag:
  print("yes")
else:
  print("no")
