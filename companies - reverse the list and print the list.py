n = int(input())
l = input().split()
s = '->'.join(x for x in l[::-1])
print(s)
