n = int(input())
l = input().split()
l = [int(x) for x in l]
min = l[0]
ans = 0
for i in range(n):
    if min > l[i]:
        min = l[i]
        ans = i
print("Dealer", end = "")
if ans == 0:
    print(1)
else:
    print(ans)
