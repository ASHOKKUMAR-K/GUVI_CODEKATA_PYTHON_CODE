n = int(input())
l = input().split(" ")
large = int(l[0])
small = int(l[0])
for i in range(n):
    if large < int(l[i]):
        large = int(l[i])
    if small > int(l[i]):
        small = int(l[i])
print(large - small)     
