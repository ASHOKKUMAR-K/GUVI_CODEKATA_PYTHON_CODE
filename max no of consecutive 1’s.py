s = input()
if "1" not in s:
    print(-1)
else:
    n = s.split("0")
    m = str(max(n))
    print(m.count("1"))
