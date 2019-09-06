(a, b) = map(str, input().split(" "))
a = len(a)
b = len(b)
if a<b:
    g = a
else:
    g = b
l = []
for i in range(1,g+1):
    if a%i==0 and b%i==0:
        l.append(str(i))
if (len(l) == 1) and ('1' in l):
    print("yes")
else:
    print("no")
