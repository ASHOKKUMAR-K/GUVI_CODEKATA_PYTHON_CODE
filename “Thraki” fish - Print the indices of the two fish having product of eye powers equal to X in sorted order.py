(n, x) = map(int, input().split())
l = [int(x) for x in input().split()]
for i in range(n):
     for j in range(i+1, n):
          if l[i]*l[j] == x:
               print(i+1, j+1)
               break
