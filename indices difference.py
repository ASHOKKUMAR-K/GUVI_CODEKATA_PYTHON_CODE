n = int(input())
l = input().split(" ")
small = int(l[0])
large = int(l[0])
s = 0
la = 0
for i in range(n):
    if small > int(l[i]):
        small = int(l[i])
        s = i
    if large < int(l[i]):
        large = int(l[i])
        la = i
print(la- s)
