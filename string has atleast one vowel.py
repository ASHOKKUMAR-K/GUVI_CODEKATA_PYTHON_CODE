n = int(input())
l = []
def vowel(a):
  vowel = ('a','e','i','o','u','A','E','I','O','U')
  flag = False
  for i in range(len(a)):
    if a[i] in vowel:
      flag = True
      break
  return flag
for i in range(n):
  l.append(str(input()))
count = 0
for i in l:
  if vowel(i):
    count+=1
if count == len(l):
  print("yes")
else:
  print("no")
