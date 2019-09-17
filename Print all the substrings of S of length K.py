(s, k) = map(str, input().split())
k = int(k)
for i in range(len(s)-k+1):
  print(s[i:(i+k)], end = " ")
