n = int(input())
l = [int(x) for x in input().split(" ")]
large = l[0]
small = l[0]
s = la = 0
for i in range(n):
    if l[i] > large:
        large = l[i]
        la = i
    if l[i] < small:
        small = l[i]
        s = i
print(s+1,la+1)
