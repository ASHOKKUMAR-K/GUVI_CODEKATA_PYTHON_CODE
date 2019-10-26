(k, n) = map(int, input().split())
l = [int(x) for x in input().split()]
a = []
count = 0
for i in l:
     if i%k in a:
          count+=1
     else:
          a.append(i%k)
print(count)
