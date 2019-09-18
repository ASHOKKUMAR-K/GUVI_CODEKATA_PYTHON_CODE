n = int(input())
l = input().split()
a = []
for i in l:
     if i not in a:
          a.append(i)
print(*a)
