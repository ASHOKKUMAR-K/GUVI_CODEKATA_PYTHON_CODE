n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
l.sort(reverse=True)
for i in l:
print(i, end="")
