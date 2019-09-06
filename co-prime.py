(a, b) = map(int, input().split(" "))
if a<b:
    g = a
else:
    g = b
l = []
for i in range(1,g+1):
    if a%i==0 and b%i==0:
        l.append(str(i))
if (len(l) == 1) and ('1' in l):
    print(1)
else:
    print(0)
