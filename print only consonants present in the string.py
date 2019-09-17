a = input()
n=len(a)
b=['a','e','i','o','u','A','E','I','O','U']
for i in range(n):
  if a[i] not in b:
    print(a[i],end="")
