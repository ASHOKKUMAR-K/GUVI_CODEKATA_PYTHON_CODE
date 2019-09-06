n=int(input())
a = []
for i in range(2, n+1):
    if n%i==0:
        a.append(i)
for i in a:
    if i % 2 == 0:
        print(i, end=" ")
