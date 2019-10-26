n, s = map(int, input().split())
l = [int(x) for x in input().split()]
l.sort(reverse = True)
count = 0
for i in range(n):
     while True:
          if l[i] <= s:
               count += 1
               s -= l[i]
          else:
               break
print(count)
