a = str(input())
b = str(input())
flag = True
for i in b:
    if i in a:
        flag = False
ln = len(a) + len(b)
if ln == 26 and flag:
    print("complementary")
else:
    print("non-complementary")
