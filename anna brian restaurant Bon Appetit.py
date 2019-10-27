(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
bc = int(input())
ba = 0
for i in range(n):
     if i != k:
          ba += (l[i] / 2)
ba = int(ba)
if ba == bc: print("Bon Appetit")
else: print(bc - ba)
