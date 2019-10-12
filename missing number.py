n = int(input())
l = [int(x) for x in input().split()]
for i in range(1, n+1):
    if i not in l:
        print(i)
        break
