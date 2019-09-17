n,k= map(int,input().split())
a= list(map(int,input().split()))
t=0
for i in range(n-1):
  for j in range(i+1,n):
    if a[i]+a[j]==k:
      t=1
      break
if t==1: print("yes")
else: print("no")
