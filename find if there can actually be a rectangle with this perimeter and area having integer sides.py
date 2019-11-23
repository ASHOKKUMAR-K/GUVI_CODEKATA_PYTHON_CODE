def isPrime(n):
  t=1
  for i in range(2,int(n/2)):
    if n%i==0 :
      t=0
      break
  if t==1 :
    return 1
  else:
    return 0
a,b= map(int,input().split())
if a%2==1 or isPrime(b):
  print("no")
else:
  print("yes")
