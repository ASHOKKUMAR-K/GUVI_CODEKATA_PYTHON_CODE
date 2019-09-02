n = int(input())
l = input().split(" ")
bit = int(l[0])
for i in l:
  bit = bit | int(i)
print(bit)
