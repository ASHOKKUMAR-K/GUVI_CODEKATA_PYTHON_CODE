(s, m)= map(str, input().split())
if len(s)!=len(m):
    mi = min(len(s), len(m))
    print(s[:mi], end = "")
    print(m[:mi], end = "")
else:
    print(s, end = "")
    print(m, end = "")
