n = int(input())
bit = int(input())
a = list(str(bin(n))[2:])
a.reverse()
if a[bit] == '1': print('true')
else: print('False')
